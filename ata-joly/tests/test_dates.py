import os
import tempfile
import unittest
from datetime import datetime
from unittest.mock import patch
from zoneinfo import ZoneInfo

import app as site


class DatesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old_dir, self.old_bookings = site.DATA_DIR, site.BOOKINGS_FILE
        site.DATA_DIR = self.tmp.name
        site.BOOKINGS_FILE = os.path.join(self.tmp.name, "bookings.json")
        site.app.testing = True
        self.client = site.app.test_client()

    def tearDown(self):
        site.DATA_DIR, site.BOOKINGS_FILE = self.old_dir, self.old_bookings
        self.tmp.cleanup()

    def apply(self, when):
        self.client.get("/book")
        with self.client.session_transaction() as session:
            token = session["csrf_token"]
        return self.client.post("/book", data={
            "csrf_token": token, "name": "Test guest",
            "contact": "test@example.com", "people": "2",
            "preferred_date": when,
        })

    def test_dates_page_and_prefill(self):
        planned = site.upcoming_departures()
        self.assertTrue(planned)
        day = planned[0]["start"]
        page = self.client.get("/dates")
        self.assertIn(day.encode(), page.data)
        self.assertIn(b"Planned", page.data)
        self.assertNotIn(b"Applications: 0", page.data)
        book = self.client.get(f"/book?date={day}")
        self.assertIn(f'value="{day}" selected'.encode(), book.data)

    def test_only_planned_dates_are_accepted(self):
        self.apply("2099-01-01")
        self.assertEqual(site.load_bookings(), [])
        day = site.upcoming_departures()[0]["start"]
        self.apply(day)
        self.assertEqual(site.load_bookings()[0]["preferred_date"], day)

    def test_old_dates_are_hidden(self):
        class FutureClock:
            @staticmethod
            def now(zone):
                return datetime(2027, 4, 1, tzinfo=ZoneInfo("Asia/Aqtau"))

        with patch.object(site, "datetime", FutureClock):
            starts = [d["start"] for d in site.upcoming_departures()]
        self.assertNotIn("2026-10-17", starts)
        self.assertIn("2027-04-10", starts)


if __name__ == "__main__":
    unittest.main()