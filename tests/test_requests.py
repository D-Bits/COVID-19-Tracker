"""
Unit tests for DataFrames
"""
from unittest import TestCase
from config import usa_cases, summary


# Test requests to API endpoints
class RequestsTests(TestCase):

    # Test response codes from API endpoints
    def test_endpoints(self):

        self.assertEqual(summary.status_code, 200)