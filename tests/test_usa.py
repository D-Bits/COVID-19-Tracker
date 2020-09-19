from unittest import TestCase
from app import app

"""
Unit testing for routes in U.S. data blueprint
"""

class USRoutesTests(TestCase):

    def test_us_summary(self):

        with app.test_client() as tc:

            response = tc.get('/us/summary')

    def test_us_cases(self):

        with app.test_client() as tc:

            response = tc.get('/us/cases')

    def test_us_deaths(self):

        with app.test_client() as tc:

            response = tc.get('/us/deaths')

    def test_us_visualizations(self):

        with app.test_client() as tc:

            response = tc.get('/us/graphs/wa')
