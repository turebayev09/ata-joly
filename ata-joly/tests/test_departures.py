import os
import tempfile
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch
from zoneinfo import ZoneInfo

import app as site


class DeparturesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.first = (datetime.now(ZoneInfo("Asia/Aqtau")).date() + timedelta(days=30)).isoformat()
        self.second = (datetime.now(ZoneInfo("Asia/Aqtau")).date() + timedelta(days=44)).isoformat()
        self.env = patch.dict(os.environ, {"TOUR_DATES": f"{self.first},{self.second}"})
        self.env.start()
        self.original_dir = site.DATA_DIR
        self.original_bookings = site.BOOKINGS_FILE
        self.original_db = site.DATABASE_URL
        site.DATA_DIR = self.tmp.name
        site.BOOKINGS_FILE = os.path.join(self.tmp.name, "bookings.json")
        site.DATABASE_URL = None
        site.app.testing = True
        self.client = site.app.test_client()

    def tearDown(self):
        self.env.stop()
        site.DATA_DIR = self.original_dir
        site.BOOKINGS_FILE = self.original_bookings
        site.DATABASE_URL = self.original_db
        self.tmp.cleanup()

    def apply(self, when, people):
        self.client.get("/book")
        with self.client.session_transaction() as sess:
            token = sess["csrf_token"]
        return self.client.post("/book", data={
            "csrf_token": token,
            "name": "Test guest", "contact": "test@example.com",
            "people": str(people), "preferred_date": when, "message": "",
        })

    def test_dates_page_and_separate_counts(self):
        response = self.client.get("/dates")
        self.assertIn(self.first.encode(), response.data)
        self.assertIn(self.second.encode(), response.data)
        self.assertIn(b"Applications: 0 people", response.data)
        self.apply(self.first, 3)
        self.apply(self.second, 2)
        response = self.client.get("/dates")
        self.assertIn(b"Applications: 3 people", response.data)
        self.assertIn(b"Applications: 2 people", response.data)
        self.assertEqual(len(site.load_bookings()), 2)

    def test_rejects_unknown_and_oversubscribed_dates(self):
        self.apply("2099-01-01", 1)
        self.apply(self.first, 9)
        response = self.apply(self.first, 2)
        self.assertIn(b"no longer has enough places", response.data)
        self.assertEqual([b["people"] for b in site.load_bookings()], [9])

    def test_no_unannounced_departures(self):
        with patch.dict(os.environ, {"TOUR_DATES": ""}):
            self.assertIn(b"No dates have been announced yet", self.client.get("/dates").data)
            self.assertIn(b"No dates have been announced yet", self.client.get("/book").data)
            self.assertEqual(site.departures(), [])


if __name__ == "__main__":
    unittest.main()