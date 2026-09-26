# -*- coding: utf-8 -*-
"""
Ata Joly — tour site + host-family registration, in Flask.

Run locally:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000

Language is stored in the browser session, switched via the nav buttons
(no page-specific translation files needed — see translations.py).

--- Security notes (read SECURITY.md for the full picture) ---
This app now requires a few environment variables before it will start in
production mode. See SECURITY.md for how to generate and set them on Render.
"""

import functools
import hmac
import json
import os
import secrets
import sys
import threading
import time
from datetime import datetime

from flask import (
    Flask, render_template, request, redirect, url_for, session, abort, Response
)
from werkzeug.security import check_password_hash

from translations import TRANSLATIONS, LANGUAGES, DEFAULT_LANG

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Environment / mode
# ---------------------------------------------------------------------------
# IS_PRODUCTION is true on Render because Render sets RENDER=true automatically.
# Locally (plain `python app.py`) it's false, so the checks below don't block
# you while you're developing on your own machine.
IS_PRODUCTION = os.environ.get("RENDER") is not None

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    if IS_PRODUCTION:
        # Refuse to boot in production without a real secret — a guessable
        # session secret lets someone forge session cookies.
        sys.exit(
            "SECRET_KEY environment variable is not set. "
            "Generate one with: python -c \"import secrets; print(secrets.token_hex(32))\" "
            "and add it in Render under Environment."
        )
    # Local dev only: a random key that's fine because it's thrown away when the process exits.
    SECRET_KEY = secrets.token_hex(32)
    print("[dev] No SECRET_KEY set — using a temporary random key for this run only.")

app.secret_key = SECRET_KEY

# Cookies: not readable by JS, not sent cross-site, HTTPS-only once deployed.
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=IS_PRODUCTION,
)

# Debug mode is controlled by an env var and defaults OFF. It must never be on
# in production — Flask's debugger lets visitors run arbitrary Python code.
DEBUG = os.environ.get("FLASK_DEBUG") == "1" and not IS_PRODUCTION

# ---------------------------------------------------------------------------
# Admin auth for /hosts and /bookings
# ---------------------------------------------------------------------------
# Set these in Render's Environment tab. Generate the hash locally with:
#   python generate_admin_hash.py
# and paste the printed hash as ADMIN_PASSWORD_HASH — never store the plain
# password anywhere, including here.
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH")

if IS_PRODUCTION and not (ADMIN_USERNAME and ADMIN_PASSWORD_HASH):
    sys.exit(
        "ADMIN_USERNAME / ADMIN_PASSWORD_HASH are not set. The /hosts and /bookings "
        "pages contain other people's phone numbers and must not be public. "
        "Run generate_admin_hash.py locally, then set both variables in Render."
    )


def require_admin(view):
    """HTTP Basic Auth gate for admin-only pages. Browsers show a native login prompt."""
    @functools.wraps(view)
    def wrapped(*args, **kwargs):
        auth = request.authorization
        if not (ADMIN_USERNAME and ADMIN_PASSWORD_HASH):
            # Local dev with no admin credentials configured: allow through with a warning,
            # so you can still see the pages while building, but never in production
            # (blocked above at startup instead).
            return view(*args, **kwargs)
        valid_user = bool(auth) and hmac.compare_digest(auth.username or "", ADMIN_USERNAME)
        valid_pass = bool(auth) and check_password_hash(ADMIN_PASSWORD_HASH, auth.password or "")
        if not (valid_user and valid_pass):
            return Response(
                "Authentication required.", 401,
                {"WWW-Authenticate": 'Basic realm="Ata Joly admin"'},
            )
        return view(*args, **kwargs)
    return wrapped


# ---------------------------------------------------------------------------
# Security headers (applied to every response)
# ---------------------------------------------------------------------------
@app.after_request
def set_security_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    resp.headers["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"
    # Allows our two font/style hosts and inline styles (the templates use a
    # few inline style="" attributes); blocks everything else by default.
    resp.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src https://fonts.gstatic.com; "
        "img-src 'self' data:; "
        "script-src 'self'; "
        "frame-ancestors 'none'"
    )
    if IS_PRODUCTION:
        resp.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains"
    return resp


# ---------------------------------------------------------------------------
# Very small in-memory rate limiter for the two public forms.
# Good enough for a school-project scale of traffic on a single instance;
# it resets whenever the process restarts, and won't work correctly if you
# ever scale to more than one instance (fine for the free Render plan).
# ---------------------------------------------------------------------------
_rate_lock = threading.Lock()
_rate_hits = {}  # ip -> [timestamps]
RATE_LIMIT = 5          # max submissions
RATE_WINDOW = 600        # per this many seconds (10 minutes)


def rate_limited(ip):
    now = time.time()
    with _rate_lock:
        hits = [t for t in _rate_hits.get(ip, []) if now - t < RATE_WINDOW]
        hits.append(now)
        _rate_hits[ip] = hits
        return len(hits) > RATE_LIMIT


def client_ip():
    # Render sits behind a proxy; the real visitor IP is in X-Forwarded-For.
    forwarded = request.headers.get("X-Forwarded-For", "")
    return forwarded.split(",")[0].strip() if forwarded else request.remote_addr


# ---------------------------------------------------------------------------
# CSRF protection for the two POST forms (hand-rolled, no extra dependency)
# ---------------------------------------------------------------------------
def get_csrf_token():
    if "csrf_token" not in session:
        session["csrf_token"] = secrets.token_hex(16)
    return session["csrf_token"]


def csrf_valid():
    token = session.get("csrf_token")
    submitted = request.form.get("csrf_token")
    return bool(token) and bool(submitted) and hmac.compare_digest(token, submitted)


app.jinja_env.globals["csrf_token"] = get_csrf_token

# ---------------------------------------------------------------------------
# Data storage — flat JSON files.
# Fine for a school project's scale. Two real limitations, both in SECURITY.md:
# it's not safe for concurrent writers beyond a single process, and on Render's
# free tier the disk is wiped on every redeploy.
# ---------------------------------------------------------------------------
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
HOSTS_FILE = os.path.join(DATA_DIR, "host_families.json")
BOOKINGS_FILE = os.path.join(DATA_DIR, "bookings.json")
_write_lock = threading.Lock()

# Max people on the next departure. Matches the "6-10 guests" the site already advertises.
GROUP_CAPACITY = 10

# Server-side field length caps, independent of whatever the HTML form allows,
# since a form's maxlength is only a suggestion to real browsers.
MAX_SHORT = 120
MAX_LONG = 800


def clamp(value, limit):
    return value[:limit]


def _ensure_data_file(path):
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def _load(path):
    _ensure_data_file(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(path, entry):
    with _write_lock:
        rows = _load(path)
        rows.append(entry)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)


def load_hosts():
    return _load(HOSTS_FILE)


def save_host(entry):
    _save(HOSTS_FILE, entry)


def load_bookings():
    return _load(BOOKINGS_FILE)


def save_booking(entry):
    _save(BOOKINGS_FILE, entry)


def spots_left():
    booked = sum(int(b.get("people") or 0) for b in load_bookings())
    return max(GROUP_CAPACITY - booked, 0)


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
    # Only ever redirect back to our own site, never to whatever a crafted
    # Referer header says, so this can't be used as an open redirect.
    ref = request.referrer or ""
    target = ref if ref.startswith(request.host_url) else url_for("index")
    return redirect(target)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = False

    if request.method == "POST":
        if rate_limited(client_ip()):
            abort(429)
        if not csrf_valid():
            error = "csrf"
        else:
            family_name = clamp(request.form.get("family_name", "").strip(), MAX_SHORT)
            aoul = clamp(request.form.get("aoul", "").strip(), MAX_SHORT)
            phone = clamp(request.form.get("phone", "").strip(), MAX_SHORT)
            guests = clamp(request.form.get("guests", "").strip(), 10)
            rooms = clamp(request.form.get("rooms", "").strip(), MAX_LONG)
            meals = clamp(request.form.get("meals", "").strip(), MAX_LONG)
            extra = clamp(request.form.get("extra", "").strip(), MAX_LONG)
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


@app.route("/book", methods=["GET", "POST"])
def book():
    error = None
    success = False

    if request.method == "POST":
        if rate_limited(client_ip()):
            abort(429)
        if not csrf_valid():
            error = "csrf"
        else:
            name = clamp(request.form.get("name", "").strip(), MAX_SHORT)
            contact = clamp(request.form.get("contact", "").strip(), MAX_SHORT)
            people = request.form.get("people", "").strip()
            preferred_date = clamp(request.form.get("preferred_date", "").strip(), MAX_SHORT)
            message = clamp(request.form.get("message", "").strip(), MAX_LONG)

            valid_people = people.isdigit() and 0 < int(people) <= GROUP_CAPACITY

            if not (name and contact and valid_people):
                error = "required"
            else:
                save_booking({
                    "name": name,
                    "contact": contact,
                    "people": int(people),
                    "preferred_date": preferred_date,
                    "message": message,
                    "submitted_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                })
                success = True

    return render_template(
        "book.html", error=error, success=success,
        left=spots_left(), capacity=GROUP_CAPACITY,
    )


@app.route("/bookings")
@require_admin
def bookings_list():
    return render_template(
        "bookings_list.html", bookings=load_bookings(),
        left=spots_left(), capacity=GROUP_CAPACITY,
    )


@app.route("/hosts")
@require_admin
def hosts_list():
    return render_template("hosts_list.html", hosts=load_hosts())


@app.errorhandler(429)
def too_many_requests(_e):
    return render_template("error.html", code=429,
                            message="Too many submissions from this address. Please try again later."), 429


@app.errorhandler(404)
def not_found(_e):
    return render_template("error.html", code=404, message="Page not found."), 404


if __name__ == "__main__":
    _ensure_data_file(HOSTS_FILE)
    _ensure_data_file(BOOKINGS_FILE)
    app.run(debug=DEBUG)
