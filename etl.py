from config import summary_json, usa_json, engine, db_connection
from pandas.errors import EmptyDataError
from psycopg2.errors import UndefinedTable
import pandas as pd


# Clean and load data from Summary API endpoint into db
def summary_etl():

    try:
        # Load API JSON data into DataFrame
        df = pd.DataFrame(summary_json['Countries'])
        # Drop slug field from DataFrame
        cleaned_data = df.drop(['Slug'], axis=1)
        # TODO: Drop redundant rows as well
        # Write DataFrame to summary table in db
        cleaned_data.to_sql('summary', engine, index_label='id', if_exists='replace', method='multi')

    # Throw exception if DataFrame is empty
    except EmptyDataError:
        input("Error: No data in DataFrame!")
    # Throw exception if table does not exist in DB.
    except UndefinedTable:
        input("Error: Table does not exist in database! Press enter to exit.")


# Clean and load data for confirmed U.S. cases
def usa_etl():

    try:
        df = pd.DataFrame()
    except:
        pass