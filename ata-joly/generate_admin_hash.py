# -*- coding: utf-8 -*-
"""
Run this ONCE on your own computer to create the admin login for /hosts and /bookings.
It never sends anything anywhere — it just prints a hash for you to copy.

Usage:
    python generate_admin_hash.py

Then, on Render: Dashboard -> your service -> Environment, add:
    ADMIN_USERNAME       = whatever username you want to log in with
    ADMIN_PASSWORD_HASH  = the long string this script prints

Do NOT put the plain password itself into Render, into git, or into any file.
Only the hash goes in the environment variable.
"""

import getpass

from werkzeug.security import generate_password_hash

if __name__ == "__main__":
    password = getpass.getpass("Choose an admin password (won't be shown): ")
    confirm = getpass.getpass("Type it again to confirm: ")

    if password != confirm:
        print("Those didn't match — run the script again.")
    elif len(password) < 8:
        print("Use at least 8 characters.")
    else:
        print("\nADMIN_PASSWORD_HASH=")
        print(generate_password_hash(password))
        print("\nCopy the line above into Render's Environment tab, together with")
        print("ADMIN_USERNAME set to whatever username you want to log in with.")
