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

    # Test about continents route
    def test_continents_route(self):

        with app.test_client() as tc:

            response = tc.get('/continents')
            self.assertEqual(response.status_code, 200)

    # Test total cases route
    def test_total_cases_route(self):

        with app.test_client() as tc:

            response = tc.get('/total_cases')
            self.assertEqual(response.status_code, 200)

    # Test new cases route
    def test_new_cases_route(self):

        with app.test_client() as tc:

            response = tc.get('/new_cases')
            self.assertEqual(response.status_code, 200)

    # Test total recoveries route
    def test_total_recoveries_route(self):

        with app.test_client() as tc:

            response = tc.get('/total_recoveries')
            self.assertEqual(response.status_code, 200)

    # Test new cases route
    def test_new_recoveries_route(self):

        with app.test_client() as tc:

            response = tc.get('/new_recoveries')
            self.assertEqual(response.status_code, 200)

    # Test demographic route
    def test_demographic_route(self):

        with app.test_client() as tc:

             response = tc.get('/demographics')
             self.assertEqual(response.status_code, 200)

    # Test total deaths route
    def test_total_deaths_route(self):

        with app.test_client() as tc:

            response = tc.get('/total_deaths')
            self.assertEqual(response.status_code, 200)

    # Test new cases route
    def test_new_deaths_route(self):

        with app.test_client() as tc:

            response = tc.get('/new_deaths')
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

    def test_world_vaccination(self):

        with app.test_client() as tc:
            
            response = tc.get('/vaccinations')
            self.assertEqual(response.status_code, 200)
