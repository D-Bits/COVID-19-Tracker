"""
Unit tests for DataFrames
"""
from unittest import TestCase
from config import usa_json, summary_json
import pandas as pd 


class DataFrameTests(TestCase):

    # Test the amount of records extracted from the summary API endpoint
    def test_summary_length(self):

        df = pd.DataFrame(summary_json["Countries"])

        self.assertEqual(len(df), 233)

    # Test the amount of records extract from the live USA cases API endpoint
    def test_usa_length(self):

        df = pd.DataFrame(usa_json)

        self.assertEqual(len(df), 17523)