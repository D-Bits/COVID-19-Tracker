"""
Summary of COVID-19 data per country.
"""
from config import summary_json
import pandas as pd 


def all_cases():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 98, 165, 171, 199, 219])

    return cleaned_data


print(all_cases())