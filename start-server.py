"""Start the Lucid server as a background process (keeps running after this exits).

If the site link stops working, run this again:
    python3 start-server.py
The public URL is printed in the server log (/tmp/lucid-server.log).
"""
import subprocess

LOG = "/tmp/lucid-server.log"
cmd = ["python3", "-u", "server.py"]

with open(LOG, "wb") as log:
    subprocess.Popen(
        cmd,
        stdin=subprocess.DEVNULL,
        stdout=log,
        stderr=log,
        start_new_session=True,   # detach from this shell's process group
        close_fds=True,
    )

print("Server starting in background. Log:", LOG)