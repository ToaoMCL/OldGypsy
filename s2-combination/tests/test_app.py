import pytest
from flask import url_for
from flask_testing import TestCase
from app import Clamp, app
from unittest.mock import patch

def test_clamp():
    for i in range(-10, 10):
        x = Clamp(i,0,5)
        assert 5 >= x >= 0

# Uncertian how to mock data = response.json
'''
class TestBase(TestCase):
    def create_app(self):
        return app

class TestMainPage(TestBase):
    def test_return_api(self):
        #with patch('request.json') as p:
        #p.return_value = { "card_weight":1, "constalation_weight":1 }
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 405)
'''      