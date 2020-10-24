from unittest import TestCase
from app import app

"""
Unit testing for routes in World blueprint
"""


class WorldRoutesTests(TestCase):

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

    # Test demographic route
    def test_demographic_route(self):

        with app.test_client() as tc:

             response = tc.get('/recoveries')
             self.assertEqual(response.status_code, 200)

    # Test deaths route
    def test_deaths_route(self):

        with app.test_client() as tc:

            response = tc.get('/deaths')
            self.assertEqual(response.status_code, 200)

    # Test country specific cases route, with Denmark as an example
    def test_country_cases_route(self):

        with app.test_client() as tc:

            response = tc.get('/country/Denmark')
            self.assertEqual(response.status_code, 200)

    # Test percentages route
    def test_percentages_route(self):

        with app.test_client() as tc:

            response = tc.get('/percentages')

    # Test country case history graph route
    def test_country_graphs(self):

        with app.test_client() as tc:
            
            response = tc.get('/graphs/brazil')
            self.assertEqual(response.status_code, 200)
