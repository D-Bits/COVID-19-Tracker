from config import summary_json
import pandas as pd 


# List recoveries for each country
def global_recoveries():

    try:
        df = pd.DataFrame(summary_json['Countries'])

        # Show only "NewDeaths" and "TotalDeaths", and countries names
        filtered_data = df.filter(items=['Country', 'NewRecovered', 'TotalRecovered'])
        # Drop redundant records obtained from API
        cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])

        return cleaned_data

    except Exception as ex:

        return "Unknown exception has occurred.", ex.args


# Top 20 countries with the most recoveries
def top20_recoveries():

    try:
        df = pd.DataFrame(summary_json['Countries'])

        # Show only "NewDeaths" and "TotalDeaths", and countries names
        filtered_data = df.filter(items=['Country', 'NewRecovered', 'TotalRecovered'])
        # Drop redundant records obtained from API
        cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])

        return cleaned_data.nlargest(20, 'TotalRecovered')

    except Exception as ex:
        
        return "Unknown exception has occurred.", ex.args


print(top20_recoveries())