from unittest import TestCase
from app import app

"""
Unit testing for routes
"""


class RoutesTests(TestCase):

    # Test index route(s) returns a 200 response
    def test_index_route(self):

        with app.test_client() as tc:

            response = tc.get('/')
            self.assertEqual(response.status_code, 200)


    # Test about page route
    def test_about_route(self):

        with app.test_client() as tc:

            response = tc.get('/about')
            self.assertEqual(response.status_code, 200)

    # Test cases route
    def test_cases_route(self):

        with app.test_client() as tc:

            response = tc.get('/cases')
            self.assertEqual(response.status_code, 200)

    # Test recoveries route
    def test_recoveries_route(self):

        with app.test_client() as tc:

            response = tc.get('/recoveries')
            self.assertEqual(response.status_code, 200)

    # Test deaths route
    def test_deaths_route(self):

        with app.test_client() as tc:

            response = tc.get('/deaths')
            self.assertEqual(response.status_code, 200)

    # Test country specific cases route, with Benin as an example
    def test_country_cases(self):

        with app.test_client() as tc:

            response = tc.get('/country/Denmark')
            self.assertEqual(response.status_code, 200)

    # Test country totals history route
    def test_country_cases(self):

        with app.test_client() as tc:
            
            response = tc.get('/totals/Brazil')
            self.assertEqual(response.status_code, 200)

    # Test country case history graph route
    def test_cases_graph(self):

        with app.test_client() as tc:
            
            response = tc.get('/graphs/cases/United States of America')
            self.assertEqual(response.status_code, 200)