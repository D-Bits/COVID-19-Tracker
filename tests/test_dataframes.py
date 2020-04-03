"""
Unit tests for DataFrames
"""
from unittest import TestCase
from config import usa_json, summary_json
import pandas as pd 


class DataFrameTests(TestCase):

    """Test that the summary DataFrame has a certain
    number of records, after being cleaned """
    def test_df_size(self):

        df = pd.DataFrame(summary_json['Countries'])
        df = pd.DataFrame(summary_json['Countries'])
        # Drop redundant records obtained from API
        cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])

        self.assertEqual(len(cleaned_data), 215)