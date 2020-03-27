from config import summary_json, engine
from pandas.errors import EmptyDataError
import pandas as pd


# Clean and load data from Summary API endpoint into db
def summary_etl():

    try:
        # Load API JSON data into DataFrame
        df = pd.DataFrame(summary_json['Countries'])
        # Drop slug field from DataFrame
        cleaned_data = df.drop(['Slug'], axis=1)
        # Dump cleaned API data to temp CSV file
        cleaned_data.to_csv('data/summary.csv')
        # Create a cursor



        #cleaned_data.to_sql('summary', engine, index_label='id', if_exists='append', method='multi')

    # Throw exception if DataFrame is empty
    except EmptyDataError:
        input("Error: No data in DataFrame!")

