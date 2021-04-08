from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_card_response(self):
        with patch("requests.get") as cards:
            cards.return_value.text = "The Fool"

            response = self.client.get(url_for("home"))
            self.assertIn(b"The Fool", response.data)