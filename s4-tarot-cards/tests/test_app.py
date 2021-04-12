import pytest
from flask import url_for
from flask_testing import TestCase
from app import GetRandomPosFromVariable, app


def test_range_of_random_generation():
    for x in range(0,10):
        returned_value = GetRandomPosFromVariable([{"v1":1, "v2":2, "v3":3}])
        assert not returned_value > 3
        assert not returned_value < 0

class TestBase(TestCase):
    def create_app(self):
        return app

class TestMainPage(TestBase):
    def test_return_api(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 200)
        