"""
Unit tests for REST API endpoints.
"""
from unittest import TestCase

from flask.helpers import send_file
from flask.wrappers import Response
from app import app


class APITests(TestCase):
    def test_world_summary(self):

        with app.test_client() as tc:

            response = tc.get("/api/world/summary/")
            self.assertEqual(response.status_code, 200)

    def test_api_docs(self):

        with app.test_client() as tc:

            response = tc.get("/api/docs")
            self.assertEqual(response.status_code, 200)

    def test_country_histroy(self):

        with app.test_client() as tc:

            response = tc.get("/api/world/belize/")
            self.assertEqual(response.status_code, 200)

    def test_api_percentages(self):

        with app.test_client() as tc:

            response = tc.get("/api/world/percentages/")
            self.assertEqual(response.status_code, 200)

    def test_api_demographics(self):

        with app.test_client() as tc:

            response = tc.get("/api/world/demographic/")
            self.assertEqual(response.status_code, 200)

    def test_us_summary(self):

        with app.test_client() as tc:

            response = tc.get("/api/us/summary/")
            self.assertEqual(response.status_code, 200)

    def test_us_state(self):

        with app.test_client() as tc:

            response = tc.get("/api/us/state/wa/")
            self.assertEqual(response.status_code, 200)
