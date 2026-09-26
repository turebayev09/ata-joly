# Security notes for Ata Joly

You asked for a full security pass. Here's exactly what changed, what you need to
do before this is safe to run for real, and — just as important — what I could
**not** check, so you're not relying on a false sense of "audited and done."

## What I actually fixed in the code

- **No hardcoded secret key.** `SECRET_KEY` now must come from an environment
  variable. In production (on Render) the app refuses to start without one.
- **Admin pages require a login.** `/hosts` and `/bookings` used to be open to
  anyone with the link — and they contain real people's names and phone numbers.
  They now require HTTP Basic Auth. See "One-time setup" below.
- **Passwords are hashed properly.** The admin password is never stored in
  plain text anywhere — not in code, not in an environment variable. You
  generate a hash locally with `generate_admin_hash.py`, and only the hash
  goes into Render.
- **CSRF protection** on both forms (`/register`, `/book`) — a hidden token
  tied to your session, checked on submit.
- **Rate limiting** — 5 submissions per 10 minutes per IP address on both
  forms, to make it harder to spam either one.
- **Security headers** on every response: `X-Content-Type-Options`,
  `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, a restrictive
  `Content-Security-Policy`, and `Strict-Transport-Security` in production.
- **Debug mode is off by default**, and cannot be turned on in production —
  it's gated behind an env var that's ignored whenever `RENDER` is set.
- **Session cookies** are HttpOnly, SameSite=Lax, and Secure in production.
- **Input length limits enforced server-side** (not just in the HTML, which
  anyone can bypass) — 120 characters for short fields, 800 for long ones.
- **Open-redirect fix** on the language switcher — it used to trust
  `Referer` blindly; now it only redirects back to this same site.
- **`data/*.json` and `.env` added to `.gitignore`** — the files that will
  hold real people's phone numbers must never end up committed to a public
  GitHub repo.

## One-time setup you need to do before this goes live

Run this on your own computer (not on Render, not in a chat):
```bash
python generate_admin_hash.py
```
It'll ask you to type a password twice and print something like:
```
ADMIN_PASSWORD_HASH=
scrypt:32768:8:1$....(long string)....
```

Then in Render: **Dashboard → your service → Environment**, add these three
variables:

| Key | Value |
|---|---|
| `SECRET_KEY` | run `python -c "import secrets; print(secrets.token_hex(32))"` locally, paste the result |
| `ADMIN_USERNAME` | any username you want, e.g. `azat` |
| `ADMIN_PASSWORD_HASH` | the hash the script printed — not the password itself |

Without these three, the app will refuse to start in production (on purpose —
better a clear error on deploy than a silently insecure site).

## What I could NOT check, and why — be honest with yourself about these

- **Your git history.** I don't have access to your actual GitHub repo (only
  to Render, for deploys and logs). If an old commit ever included a real
  secret — a password, an API key, your actual `SECRET_KEY` — deleting it in
  a new commit does **not** remove it from history; it's still fetchable.
  If you're worried something leaked, the fix is `git filter-repo` or the
  BFG Repo-Cleaner to scrub history, or — simpler and more reliable —
  rotate whatever leaked (change the password / regenerate the key) and
  treat the old one as burned.
- **Your actual Render environment variables.** I can't read them from here;
  I can only tell you which ones the code now requires.
- **A real vulnerability scan of your dependencies.** I checked that
  `Flask==3.0.3` / `Werkzeug==3.1.8` / `gunicorn==22.0.0` don't have
  known critical CVEs affecting a normal (non-debug) deployment as of my
  last check, but I don't have a live feed of new CVEs. Before anything
  important, run:
  ```bash
  pip install pip-audit --break-system-packages
  pip-audit -r requirements.txt
  ```
- **"API keys"** — this app doesn't call any third-party API and doesn't
  have any API keys to leak. If you add one later (e.g. for email
  notifications), put it in an environment variable immediately, never in
  code, and add it to `.gitignore` if it lives in a local file.
- **The database** — there isn't one; data is flat JSON files on disk. That's
  fine for a school project's scale, but it means: no encryption at rest,
  no real access control beyond the admin login, and — on Render's free
  tier — the data is wiped on every redeploy. If this becomes a real
  service, move to Postgres (Render has a free tier for that too) before
  collecting real people's data.

## Realistic scope check

This is now reasonably hardened for what it is: a small school-project
booking site with two public forms and an admin view. It is **not** hardened
to the standard of a service that handles payments, stores passwords for
many users, or needs to survive a dedicated attacker. If this ever grows
past "class demo," the next real steps would be: a proper database, real
user accounts instead of one shared admin login, server-side logging and
monitoring, and a second pair of eyes (or a paid pentest) before handling
anything sensitive like actual payments.
