"""
Unit tests for DataFrames
"""
from unittest import TestCase
from config import summary
from requests import get


# Test requests to API endpoints
class RequestsTests(TestCase):

    # Test response code from the summary API endpoint
    def test_summary_endpoint(self):

        self.assertEqual(summary.status_code, 200)

    # Test response code for an individual country's cases
    def test_country_endpoint(self):

        endpoint = get('https://api.covid19api.com/live/country/south-africa/status/confirmed')

        self.assertEqual(endpoint.status_code, 200)