from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app, Fortune, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Fortune(card_name="The Bool", card_weight=1, constalation_name="eo", constalation_weight=1, luck=20, fortune="Good fortune"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_card_response_normal_luck(self):
        with requests_mock.mock() as front_end_requests:
            front_end_requests.get("http://constilations:5002/get/constalation", json = {"constalation_name":"Leo", "constalation_weight":1} )
            front_end_requests.get("http://tarot-cards:5003/get/card", json = {"card_name":"The Fool", "card_weight":4} ) 
            front_end_requests.post("http://combination:5001/get/premonition", json= { "card_name":"The Fool", "card_weight":1, "constalation_name":"Leo", "constalation_weight":1, "luck":6 } )
            response = self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Your fortune bears the color beige", response.data)

    def test_card_response_low_luck(self):
        with requests_mock.mock() as front_end_requests:
            front_end_requests.get("http://constilations:5002/get/constalation", json = {"constalation_name":"Leo", "constalation_weight":1} )
            front_end_requests.get("http://tarot-cards:5003/get/card", json = {"card_name":"The Fool", "card_weight":3} ) 
            front_end_requests.post("http://combination:5001/get/premonition", json= { "card_name":"The Fool", "card_weight":1, "constalation_name":"Leo", "constalation_weight":1, "luck":2 } )
            response = self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Your fortune looks bleak", response.data)
    
    def test_card_response_high_luck(self):
        with requests_mock.mock() as front_end_requests:
            front_end_requests.get("http://constilations:5002/get/constalation", json = {"constalation_name":"Leo", "constalation_weight":1} )
            front_end_requests.get("http://tarot-cards:5003/get/card", json = {"card_name":"The Fool", "card_weight":2} ) 
            front_end_requests.post("http://combination:5001/get/premonition", json= { "card_name":"The Fool", "card_weight":1, "constalation_name":"Leo", "constalation_weight":1, "luck":20 } )
            response = self.client.get(url_for("home"))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Good fortune awaits you", response.data)

    def test_db_entry_is_readable(self):
        response = self.client.get(url_for("past_fortunes"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Bool", response.data)
        self.assertIn(b"1", response.data)
        self.assertIn(b"20", response.data)
        self.assertNotIn(b"7", response.data)


