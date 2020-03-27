from config import summary_json, engine, db_connection
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
        # Write DataFrame to summary table in db
        cleaned_data.to_sql('summary', engine, index_label='id', if_exists='append', method='multi')

    # Throw exception if DataFrame is empty
    except EmptyDataError:
        input("Error: No data in DataFrame!")
    # Throw exception if table does not exist in DB.
    except UndefinedTable:
        input("Error: Table does not exist in database! Press enter to exit.")
    # Throw exception is data source cannot be found
    except FileNotFoundError:
        input('Error: Data source cannot be found! Press enter to exit.')

