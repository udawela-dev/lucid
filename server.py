"""Lucid waitlist server — Python stdlib only.

Serves the static build-lab/ directory, handles POST /api/waitlist
with SQLite persistence, the founder sign-in (sessions), a private
dashboard (/dashboard) that lists everyone who joined, and optional
email notifications when someone joins (see email_config.py).

No npm packages, no framework.

Run: python3 build-lab/server.py
Then visit: http://localhost:3000/  (or the Codio public URL)
"""

import json
import os
import re
import secrets
import smtplib
import sqlite3
from email.message import EmailMessage
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

# ── configuration ──────────────────────────────────────────────────────
PORT = int(os.environ.get("PORT", "3000"))
# all files live under /home/codio/workspace/build-lab (Codio workspace)
BUILD_LAB = "/home/codio/workspace/build-lab"
DB_PATH = os.path.join(BUILD_LAB, "waitlist.db")
STATIC_DIR = BUILD_LAB
PREFIX = "/api/waitlist"
SIGNIN_PREFIX = "/api/signin"
SIGNUP_PREFIX = "/api/signup"
LOGOUT_PREFIX = "/api/logout"
WAITLIST_EMAIL_PREFIX = "/api/waitlist/email"
WAITLIST_DELETE_PREFIX = "/api/waitlist/delete"
SESSION_COOKIE = "lucid_session"

# email settings — safe defaults, real values come from email_config.py
SENDER_EMAIL = ""
SENDER_PASSWORD = ""
NOTIFY_EMAIL = "udawelashanwick@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
try:
    from email_config import (
        SENDER_EMAIL,
        SENDER_PASSWORD,
        NOTIFY_EMAIL,
        SMTP_SERVER,
        SMTP_PORT,
    )
    # app passwords often contain spaces; remove them
    SENDER_PASSWORD = SENDER_PASSWORD.replace(" ", "")
except ImportError:
    pass  # email_config.py missing → email just gets skipped

# ── database ───────────────────────────────────────────────────────────
def _get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS waitlist "
        "(id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    # if the table already existed without the name column, add it
    try:
        conn.execute("ALTER TABLE waitlist ADD COLUMN name TEXT")
    except sqlite3.OperationalError:
        pass  # column already exists
    conn.execute(
        "CREATE TABLE IF NOT EXISTS signin "
        "(id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    # if the table already existed without the name column, add it
    try:
        conn.execute("ALTER TABLE signin ADD COLUMN name TEXT")
    except sqlite3.OperationalError:
        pass  # column already exists
    conn.execute(
        "CREATE TABLE IF NOT EXISTS sessions "
        "(token TEXT PRIMARY KEY, email TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    # every email Lucid generates is recorded here so the founder can see
    # them even before a real email sender is configured
    conn.execute(
        "CREATE TABLE IF NOT EXISTS outbox "
        "(id INTEGER PRIMARY KEY, recipient TEXT, subject TEXT, body TEXT, "
        "status TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    )
    conn.commit()
    return conn


# ── email helper ───────────────────────────────────────────────────────
def _send_email(subject, body, recipients):
    """Send one email to a list of recipients.

    Every email is always saved to the outbox table first, so the founder
    can see what was generated even before a real sender is configured.

    Returns True when a real email was sent, False when it was only saved
    to the outbox (no sender configured yet, or sending failed).
    Never raises — the website must keep working even without email.
    """
    conn = _get_db()
    outbox_ids = []
    for recipient in recipients:
        cur = conn.execute(
            "INSERT INTO outbox (recipient, subject, body, status) VALUES (?, ?, ?, 'pending')",
            (recipient, subject, body),
        )
        outbox_ids.append(cur.lastrowid)
    conn.commit()
    conn.close()

    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("[email] NOT configured — email stored in the outbox (see /dashboard)")
        return False

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(recipients)
    msg.set_content(body)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        # real email went out — mark the outbox copies as sent
        conn = _get_db()
        for row_id in outbox_ids:
            conn.execute("UPDATE outbox SET status = 'sent' WHERE id = ?", (row_id,))
        conn.commit()
        conn.close()
        print(f"[email] sent: {subject} → {len(recipients)} recipient(s)")
        return True
    except Exception as exc:  # noqa: BLE001 — log and continue
        print(f"[email] failed: {exc}")
        return False


# ── request handler ────────────────────────────────────────────────────
class Handler(BaseHTTPRequestHandler):
    # suppress default stderr logging for cleaner output
    def log_message(self, format, *args):
        pass

    # ---- helpers -------------------------------------------------------
    def _get_cookie(self, name):
        cookies = self.headers.get("Cookie", "")
        for part in cookies.split(";"):
            part = part.strip()
            if part.startswith(name + "="):
                return part[len(name) + 1:]
        return None

    def _get_session_email(self):
        """Return the signed-in founder's email, or None."""
        token = self._get_cookie(SESSION_COOKIE)
        if not token:
            return None
        conn = _get_db()
        row = conn.execute(
            "SELECT email FROM sessions WHERE token = ?", (token,)
        ).fetchone()
        conn.close()
        return row[0] if row else None

    def _send_json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # ---- routes --------------------------------------------------------
    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self._send_html("index.html")
        elif path == "/waitlist-thanks":
            self._send_html("waitlist-thanks.html")
        elif path == "/signin":
            self._send_html("signin.html")
        elif path == "/signup":
            self._send_html("signup.html")
        elif path == "/email-help":
            self._send_html("email-help.html")
        elif path == "/dashboard":
            if self._get_session_email():
                self._send_html("dashboard.html")
            else:
                self._send_redirect("/signin")
        elif path == "/api/waitlist":
            self._handle_waitlist_list()
        elif path == "/api/outbox":
            self._handle_outbox()
        elif path.startswith("/build-l/"):
            # allow Build Lab relative paths if needed
            self._send_static(self.path[len("/build-l/"):])
        else:
            # serve any static file (style.css, script.js, etc.)
            self._send_static(path.lstrip("/"))

    def do_POST(self):
        path = urlparse(self.path).path
        if path == PREFIX:
            self._handle_waitlist()
        elif path == SIGNIN_PREFIX:
            self._handle_signin()
        elif path == SIGNUP_PREFIX:
            self._handle_signup()
        elif path == LOGOUT_PREFIX:
            self._handle_logout()
        elif path == WAITLIST_EMAIL_PREFIX:
            self._handle_waitlist_email()
        elif path == WAITLIST_DELETE_PREFIX:
            self._handle_waitlist_delete()
        else:
            self._send_404()

    # ---- static files --------------------------------------------------
    def _send_html(self, filename):
        filepath = os.path.join(STATIC_DIR, filename)
        if not os.path.exists(filepath):
            self._send_404()
            return
        with open(filepath, "r", encoding="utf-8") as f:
            body = f.read().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_static(self, filename):
        filepath = os.path.join(STATIC_DIR, filename)
        if not os.path.exists(filepath):
            self._send_404()
            return
        with open(filepath, "rb") as f:
            body = f.read()
        ctype = "text/plain"
        if filename.endswith(".css"):
            ctype = "text/css"
        elif filename.endswith(".js"):
            ctype = "application/javascript"
        elif filename.endswith(".svg"):
            ctype = "image/svg+xml"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_redirect(self, location):
        self.send_response(302)
        self.send_header("Location", location)
        self.end_headers()

    def _send_404(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"<h1>404 Not Found</h1>")

    # ---- waitlist (join) ----------------------------------------------
    def _handle_waitlist(self):
        content_length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_length)
        try:
            data = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            self._send_json(400, {"status": "error", "message": "Invalid JSON"})
            return

        email = data.get("email", "").strip()
        name = data.get("name", "").strip()

        if not email or "@" not in email or "." not in email.split("@")[-1]:
            self._send_json(400, {"status": "error", "message": "Please enter a valid email address"})
            return

        # store in SQLite (INSERT OR IGNORE handles duplicates gracefully)
        conn = _get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT OR IGNORE INTO waitlist (name, email) VALUES (?, ?)",
            (name or None, email),
        )
        affected = cur.rowcount  # 1 = new row, 0 = duplicate ignored
        conn.commit()
        conn.close()

        if affected == 1:
            # welcome email to the new joiner
            _send_email(
                "Welcome to Lucid — find a link you saved but lost",
                f"Hi{(' ' + name) if name else ''}!\n\n"
                f"Thanks for joining the Lucid waitlist. Lucid finds links you saved but lost — "
                f"across bookmarks, screenshots, and messages — from one calm search box.\n\n"
                f"We'll email you as soon as Lucid is ready.\n\n"
                f"— The Lucid team",
                [email],
            )
            # notification to the founder
            _send_email(
                "New Lucid waitlist signup",
                f"Someone new joined the Lucid waitlist!\n\n"
                f"Name: {name or '(not given)'}\n"
                f"Email: {email}\n\n"
                f"Open the dashboard to see everyone: /dashboard",
                [NOTIFY_EMAIL],
            )
            self._send_json(200, {"status": "success", "message": "You're on the way!"})
        else:
            self._send_json(200, {"status": "duplicate", "message": "You're already on the list!"})

    # ---- waitlist (list — founder only) --------------------------------
    def _handle_waitlist_list(self):
        if not self._get_session_email():
            self._send_json(401, {"status": "error", "message": "Please sign in first"})
            return
        conn = _get_db()
        rows = conn.execute(
            "SELECT name, email, created_at FROM waitlist ORDER BY id DESC"
        ).fetchall()
        conn.close()
        signups = [
            {"name": r[0] or "", "email": r[1], "created_at": r[2]}
            for r in rows
        ]
        self._send_json(200, {"status": "success", "signups": signups})

    # ---- outbox (every generated email — signed in users only) ---------
    def _handle_outbox(self):
        if not self._get_session_email():
            self._send_json(401, {"status": "error", "message": "Please sign in first"})
            return
        conn = _get_db()
        rows = conn.execute(
            "SELECT recipient, subject, status, created_at FROM outbox ORDER BY id DESC LIMIT 50"
        ).fetchall()
        conn.close()
        emails = [
            {"recipient": r[0], "subject": r[1], "status": r[2], "created_at": r[3]}
            for r in rows
        ]
        self._send_json(200, {
            "status": "success",
            "emails": emails,
            "email_configured": bool(SENDER_EMAIL and SENDER_PASSWORD),
        })

    # ---- waitlist (email everyone — founder only) ----------------------
    def _handle_waitlist_email(self):
        if not self._get_session_email():
            self._send_json(401, {"status": "error", "message": "Please sign in first"})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_length)
        try:
            data = json.loads(raw) if raw else {}
        except (json.JSONDecodeError, ValueError):
            data = {}

        conn = _get_db()
        rows = conn.execute("SELECT name, email FROM waitlist").fetchall()
        conn.close()

        if not rows:
            self._send_json(200, {"status": "success", "message": "No one is on the list yet"})
            return

        subject = (data.get("subject", "") or "Lucid update").strip()
        subject = subject[:120]  # keep it short
        message = (data.get("message", "") or
                   "Hi, thanks for joining the Lucid waitlist! Lucid is coming soon — "
                   "we'll be in touch with news.").strip()

        recipients = [r[1] for r in rows]
        ok = _send_email(subject, message, recipients)
        if ok:
            self._send_json(200, {"status": "success", "message": f"Email sent to {len(recipients)} people"})
        else:
            self._send_json(200, {"status": "success", "message": f"Saved to the outbox for {len(recipients)} people — add a sender in email_config.py to deliver for real"})

    # ---- waitlist (delete one entry — signed in users only) -------------
    def _handle_waitlist_delete(self):
        if not self._get_session_email():
            self._send_json(401, {"status": "error", "message": "Please sign in first"})
            return

        content_length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_length)
        try:
            data = json.loads(raw) if raw else {}
        except (json.JSONDecodeError, ValueError):
            data = {}

        email = (data.get("email") or "").strip()
        if not email:
            self._send_json(400, {"status": "error", "message": "Missing email"})
            return

        conn = _get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM waitlist WHERE email = ?", (email,))
        affected = cur.rowcount
        conn.commit()
        conn.close()

        if affected == 1:
            self._send_json(200, {"status": "success", "message": "Removed from the list"})
        else:
            self._send_json(404, {"status": "error", "message": "No one with that email is on the list"})

    # ---- sign-in -------------------------------------------------------
    def _start_session(self, email):
        """Create a session row and prepare the cookie header."""
        conn = _get_db()
        cur = conn.cursor()
        token = secrets.token_hex(16)
        cur.execute("INSERT INTO sessions (token, email) VALUES (?, ?)", (token, email))
        conn.commit()
        conn.close()
        self.send_header(
            "Set-Cookie",
            f"{SESSION_COOKIE}={token}; Path=/; HttpOnly; SameSite=Lax; Max-Age=604800",
        )

    def _handle_signin(self):
        content_length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_length)
        try:
            data = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            self._send_json(400, {"status": "error", "message": "Invalid JSON"})
            return

        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        if not email or "@" not in email or "." not in email.split("@")[-1]:
            self._send_json(400, {"status": "error", "message": "Please enter a valid email address"})
            return

        if not password or len(password) < 4:
            self._send_json(400, {"status": "error", "message": "Password must be at least 4 characters"})
            return

        conn = _get_db()
        cur = conn.cursor()

        # First-ever sign-in creates the founder account.
        has_accounts = cur.execute("SELECT 1 FROM signin LIMIT 1").fetchone()
        if not has_accounts:
            cur.execute("INSERT INTO signin (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
        else:
            match = cur.execute(
                "SELECT email FROM signin WHERE email = ? AND password = ?",
                (email, password),
            ).fetchone()
            if not match:
                conn.close()
                self._send_json(401, {"status": "error", "message": "Incorrect email or password"})
                return
        conn.close()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(json.dumps({"status": "success", "message": "Signed in"}))))
        self._start_session(email)
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success", "message": "Signed in"}).encode())

    # ---- sign-up -------------------------------------------------------
    def _handle_signup(self):
        content_length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(content_length)
        try:
            data = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            self._send_json(400, {"status": "error", "message": "Invalid JSON"})
            return

        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        password = data.get("password", "").strip()

        if not name:
            self._send_json(400, {"status": "error", "message": "Please enter your name"})
            return

        if not email or "@" not in email or "." not in email.split("@")[-1]:
            self._send_json(400, {"status": "error", "message": "Please enter a valid email address"})
            return

        if not password or len(password) < 4:
            self._send_json(400, {"status": "error", "message": "Password must be at least 4 characters"})
            return

        conn = _get_db()
        cur = conn.cursor()

        # no duplicate accounts
        existing = cur.execute("SELECT email FROM signin WHERE email = ?", (email,)).fetchone()
        if existing:
            conn.close()
            self._send_json(409, {"status": "error", "message": "An account with that email already exists"})
            return

        cur.execute("INSERT INTO signin (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()

        # welcome email to the new account owner
        _send_email(
            "Welcome to Lucid — your account is ready",
            f"Hi {name}!\n\n"
            f"Your Lucid account is ready. You can sign in any time to see the "
            f"people who joined the waitlist.\n\n"
            f"Lucid finds links you saved but lost — across bookmarks, "
            f"screenshots, and messages — from one calm search box.\n\n"
            f"Thanks for being part of it!\n"
            f"— The Lucid team",
            [email],
        )

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(json.dumps({"status": "success", "message": "Account created"}))))
        self._start_session(email)
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success", "message": "Account created"}).encode())

    # ---- sign-out ------------------------------------------------------
    def _handle_logout(self):
        token = self._get_cookie(SESSION_COOKIE)
        if token:
            conn = _get_db()
            conn.execute("DELETE FROM sessions WHERE token = ?", (token,))
            conn.commit()
            conn.close()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Set-Cookie", f"{SESSION_COOKIE}=; Path=/; Max-Age=0; HttpOnly; SameSite=Lax")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success", "message": "Signed out"}).encode())


# ── main ───────────────────────────────────────────────────────────────
def main():
    # ensure DB + tables exist on first run
    _get_db().close()

    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Lucid waitlist server running at http://0.0.0.0:{PORT}/")
    print(f"  (Codio public URL: https://{os.environ.get('CODIO_HOSTNAME','localhost')}-3000.codio.io/)")
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("  Email: NOT configured — join notifications are off until you fill in email_config.py")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()