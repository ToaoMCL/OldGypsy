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
            front_end_requests.get("http://constilations:5002/get/constalation", text= "Leo" ) 
            front_end_requests.get("http://tarot-cards:5003/get/card", text= "The Fool" ) 
            front_end_requests.get("http://combination:5001/get/premonition/a/2/b/3", text= "aaaaa" )
            response = self.client.get(url_for("home"))
            self.assertIn(b"The Fool", response.data)