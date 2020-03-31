"""
Analysis for statistics of cases per country.
"""
from config import summary_json
import pandas as pd 


def all_cases():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewConfirmed', 'TotalConfirmed'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])

    return cleaned_data


# Show the top 20 countries with the most cases
def top_20():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewConfirmed', 'TotalConfirmed'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])
    # Filter top countries
    return cleaned_data.nlargest(20, 'TotalConfirmed')


top_20()