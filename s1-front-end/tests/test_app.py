from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_card_response(self):
        with requests_mock.mock() as front_end_requests:
            #front_end_requests.get("http://oldgypsy_constilations_1:5002/get/constalation", text= "Leo" ) 
            front_end_requests.get("http://oldgypsy_tarot-cards_1:5003/get/card", text= "The Fool" ) 

            response = self.client.get(url_for("home"))
            self.assertIn(b"The Fool", response.data)