# -*- coding: utf-8 -*-
"""
Ata Joly — tour site + host-family registration, in Flask.

Run locally:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000

Language is stored in the browser session, switched via the nav buttons
(no page-specific translation files needed — see translations.py).
"""

import json
import os
import threading
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, session

from translations import TRANSLATIONS, LANGUAGES, DEFAULT_LANG

app = Flask(__name__)
app.secret_key = "change-this-before-any-real-deployment"  # fine for a school demo, not for production

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
HOSTS_FILE = os.path.join(DATA_DIR, "host_families.json")
_write_lock = threading.Lock()


def _ensure_data_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(HOSTS_FILE):
        with open(HOSTS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def load_hosts():
    _ensure_data_file()
    with open(HOSTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_host(entry):
    with _write_lock:
        hosts = load_hosts()
        hosts.append(entry)
        with open(HOSTS_FILE, "w", encoding="utf-8") as f:
            json.dump(hosts, f, ensure_ascii=False, indent=2)


def get_lang():
    lang = session.get("lang", DEFAULT_LANG)
    return lang if lang in LANGUAGES else DEFAULT_LANG


@app.context_processor
def inject_globals():
    """Makes `t` (current translation dict) and `lang` available in every template."""
    lang = get_lang()
    return {"t": TRANSLATIONS[lang], "lang": lang, "languages": LANGUAGES,
             "all_t": TRANSLATIONS}


@app.route("/set-lang/<lang_code>")
def set_lang(lang_code):
    if lang_code in LANGUAGES:
        session["lang"] = lang_code
    # send the visitor back to whatever page they switched language on
    return redirect(request.referrer or url_for("index"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = False

    if request.method == "POST":
        family_name = request.form.get("family_name", "").strip()
        aoul = request.form.get("aoul", "").strip()
        phone = request.form.get("phone", "").strip()
        guests = request.form.get("guests", "").strip()
        rooms = request.form.get("rooms", "").strip()
        meals = request.form.get("meals", "").strip()
        extra = request.form.get("extra", "").strip()
        consent = request.form.get("consent") == "on"

        if not (family_name and aoul and phone and consent):
            error = "required"
        else:
            save_host({
                "family_name": family_name,
                "aoul": aoul,
                "phone": phone,
                "guests": guests,
                "rooms": rooms,
                "meals": meals,
                "extra": extra,
                "submitted_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            })
            success = True

    return render_template("register.html", error=error, success=success)


@app.route("/hosts")
def hosts_list():
    """Simple read-only listing so the class/teacher can see registrations come through.
    No login here on purpose to keep the demo simple — add auth before using this for real."""
    return render_template("hosts_list.html", hosts=load_hosts())


if __name__ == "__main__":
    _ensure_data_file()
    app.run(debug=True)
