from unittest import TestCase
from app import app

"""
Unit testing for routes in U.S. data blueprint
"""

class USRoutesTests(TestCase):

    def test_us_summary(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary')
            self.assertEqual(response.status_code, 200)

    def test_us_cases(self):

        with app.test_client() as tc:

            response = tc.get('/us/cases')
            self.assertEqual(response.status_code, 200)

    def test_us_deaths(self):

        with app.test_client() as tc:

            response = tc.get('/us/deaths')
            self.assertEqual(response.status_code, 200)

    def test_us_visualizations(self):

        with app.test_client() as tc:

            response = tc.get('/us/graphs/wa')
            self.assertEqual(response.status_code, 200)
