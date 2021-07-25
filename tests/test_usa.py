from unittest import TestCase
from app import app

"""
Unit testing for routes in U.S. data blueprint
"""

class USRoutesTests(TestCase):

    def test_us_summary_states(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary/state')
            self.assertEqual(response.status_code, 200)

    def test_us_cases(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary/cases')
            self.assertEqual(response.status_code, 200)

    def test_hospitalizations(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary/hospitalized')
            self.assertEqual(response.status_code, 200)

    def test_hospitalization_increase(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary/hospitalization_increase')
            self.assertEqual(response.status_code, 200)

    def test_us_deaths(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary/deaths')
            self.assertEqual(response.status_code, 200)

    def test_deaths_increase(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary/deaths_increase')
            self.assertEqual(response.status_code, 200)

    def test_us_visualizations(self):

        with app.test_client() as tc:

            response = tc.get('/us/graphs/Washington')
            self.assertEqual(response.status_code, 200)
