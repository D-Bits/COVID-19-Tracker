"""
Summary of COVID-19 data per country.
"""
from config import summary_json
import pandas as pd 


def summary_data():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 98, 165, 171, 199, 219])

    return cleaned_data


# For passing into Flask routes
sum_data = summary_data()