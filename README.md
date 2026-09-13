# Ata Joly — Flask version

A tour website with a host-family registration form and EN / RU / KZ language switching.

## Run it locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in a browser.

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

## Things to know before the school presentation

- This needs Python running — it's not a file you can just double-click and open in a
  browser like the old HTML version. Either run it on your laptop during the
  presentation, or deploy it somewhere like PythonAnywhere or Render if you want a link.
- `/hosts` has no password on it. Fine for a class demo where you control who has the
  link; not fine if this ever goes on the open internet with real families' phone
  numbers in it. Add a login before that happens.
- The Kazakh translations were machine-assisted — get a native speaker to proofread
  them before you present, especially the longer paragraphs.
- Data is stored in a flat JSON file, not a real database. Perfectly fine for a school
  project's scale; would need swapping for SQLite/Postgres for anything real.
