"""
A collection of functions to analyize data
obtained from the API.
"""
from config import summary_json
import pandas as pd 


# Show deaths due to COVID-19 for each country
def global_deaths():

    try:
        df = pd.DataFrame(summary_json['Countries'])
        # Show only "NewDeaths" and "TotalDeaths", and countries names
        filtered_data = df.filter(items=['Country', 'NewDeaths', 'TotalDeaths'])
        # Drop redundant records obtained from API
        cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])

        print(cleaned_data)
    
    except:
        return "An unknown error occured. We apologize for the inconvience."


# Show the countries with the top 20 most fatalities
def top20_deaths():

    try:
        df = pd.DataFrame(summary_json['Countries'])
        # Show only "NewDeaths" and "TotalDeaths", and countries names
        filtered_data = df.filter(items=['Country', 'NewDeaths', 'TotalDeaths'])
        # Drop redundant records obtained from API
        cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])
        
        # Filter top countries
        return cleaned_data.nlargest(20, 'TotalDeaths')

    except:
        return "An unknown error occured. We apologize for the inconvience."


print(top20_deaths())