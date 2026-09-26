# Ata Joly — Flask version

A tour website with a host-family registration form and EN / RU / KZ language switching.

## Run it locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in a browser.

Locally you don't need to set anything — the app generates a temporary secret
key and leaves the admin pages open so you can see them while building.
**Before deploying, read `SECURITY.md`** — production mode requires three
environment variables and will refuse to start without them.

## What's here

- `app.py` — the Flask app: routes for the home page, the host registration form, and a
  read-only list of registered host families.
- `translations.py` — every piece of text on the site, in English, Russian and Kazakh.
  Add a language by copying one of the three dicts and translating the values.
- `templates/` — Jinja2 HTML templates. They pull all copy from `t` (the current
  language's dict), so you never need to touch the templates to change wording.
- `static/style.css` — all the styling.
- `data/host_families.json` — created automatically the first time someone submits the
  registration form. Plain JSON, easy to open and read for the demo.
- `generate_admin_hash.py` — run this once locally to set up the admin login. See `SECURITY.md`.
- `SECURITY.md` — what's been hardened, what you need to configure, and what wasn't checked.

## Things to know before the school presentation

- This needs Python running — it's not a file you can just double-click and open in a
  browser like the old HTML version. Either run it on your laptop during the
  presentation, or deploy it somewhere like PythonAnywhere or Render if you want a link.
- `/hosts` and `/bookings` now require a login (see `SECURITY.md`) — set that up before
  you deploy for real, or Render will refuse to start the app anyway.
- The Kazakh translations were machine-assisted — get a native speaker to proofread
  them before you present, especially the longer paragraphs.
- Data is stored in a flat JSON file, not a real database. Perfectly fine for a school
  project's scale; would need swapping for SQLite/Postgres for anything real.
