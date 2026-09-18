# Lucid

**Find a link you saved but lost.**

Lucid is a privacy-first personal search tool for students and beginner programmers.
Important links get scattered across bookmarks, screenshots, and messages — Lucid
finds them again from one search box.

This repository is the working product: a professional 13-section landing page that
tells the story, collects waitlist signups, and gives the founder a private
dashboard to watch everyone who joins.

---

## Live links

| What | URL |
| :--- | :--- |
| Full app (waitlist, sign-in, dashboard) | https://lorenzofashion-planetstatic-3000.codio.io/ |
| Static landing page (GitHub Pages) | https://udawela-dev.github.io/lucid/ |

> Note: GitHub Pages serves the static landing page only. The waitlist form,
> sign-in, and founder dashboard need the Python server below.

## Features

- 13-section landing page: hero, problem, solution, how it works, cross-source
  search, privacy, example results, before-vs-lucid, who it's for, features,
  social proof, founder note, FAQ, waitlist CTA
- Light, professional design system (white + light blue) with Fraunces + Inter
- **Waitlist** — name + email saved to SQLite, no duplicate entries
- **Sign up / Sign in** — anyone can create an account with their own email and
  password; sessions use secure HttpOnly cookies
- **Founder dashboard (Watch area)** — every waitlist signup (name, email, date),
  delete buttons, and a mail-outbox that records every generated email
- **Outbox** — every email Lucid would send (welcome emails, join notifications)
  is saved and visible, even before real email is configured
- Optional **Connect your email** page — add a Gmail app password to deliver
  real emails (welcome messages + "someone joined" notifications)
- 50 automated tests covering the navbar, hero, all content sections, and
  design-token quality rules

## Tech stack

- Plain **HTML, CSS, and vanilla JavaScript** — no frameworks, no build step
- **Python 3 standard library** HTTP server (`server.py`) — no frameworks
- **SQLite** for storage (`waitlist.db`, created automatically on first run)
- **Node.js** only for running the tests

## Getting started

Requirements: Python 3.11+ (Node.js only needed for tests).

```bash
cd build-lab
python3 server.py
```

The server binds to `0.0.0.0:3000` and creates the `waitlist.db` database the
first time it runs. There is also a helper that starts the server in the
background and survives terminal closes:

```bash
python3 start-server.py
```

Logs go to `/tmp/lucid-server.log`.

## Running the tests

```bash
cd build-lab/tests
node navbar-hero.test.js
node content-sections.test.js
node quality-audit.test.js
```

All 50 tests should pass.

## Repo structure

```
build-lab/
├── index.html          # the 13-section landing page
├── style.css           # design tokens + all styles
├── script.js           # page interactions (mobile menu, search demo)
├── server.py           # Python HTTP server + API + SQLite
├── dashboard.html      # founder Watch area (sign-in required)
├── signin.html         # sign-in page
├── signup.html         # sign-up page (anyone can join)
├── email-setup.html    # connect a Gmail sender (optional)
├── email-help.html     # step-by-step email setup guide
├── waitlist-thanks.html
├── assets/             # SVG visuals (hero, sources, privacy)
├── tests/              # 50 automated tests (Node)
├── MISSION.md          # founder notebook (decisions + roadmap)
└── SPECS/              # feature specifications
```

## Email (optional)

Real email delivery needs one Gmail account with a 16-character **app password**
(Gmail does not allow normal passwords for sending). Fill in `email_config.py`
or use the in-app **Connect your email** page. Without it, nothing breaks — every
email is still generated and recorded in the Outbox on the dashboard.

`email_config.py` and `waitlist.db` are gitignored, so secrets and data never
reach GitHub.

## Founder notebook

All brand, design, and product decisions live in [MISSION.md](MISSION.md).