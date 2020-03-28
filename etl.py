from config import summary_json, usa_json, engine, db_connection
from pandas.io.json import json_normalize
from pandas.errors import EmptyDataError
from psycopg2.errors import UndefinedTable
import pandas as pd


"""
Params:
- data_src = the API endpoint
- table = the db table the data is to be written to
- dropped_records = a list of row numbers to be dropped prior to ingestion, 
                    or 0 if no records are to be dropped.
"""
def data_etl(data_src, table, dropped_records):

    try:
        # Load API JSON data into DataFrame
        df = pd.DataFrame(data_src)
        # Drop slug field from DataFrame
        cleaned_data = df.drop(dropped_records)
        # Write DataFrame to summary table in db
        cleaned_data.to_sql(table, engine, index_label='id', if_exists='replace', method='multi')
        # Show the no. of records written to the db
        print(f"{len(cleaned_data)} records successfully written to {table} table.")

    # Throw exception if DataFrame is empty
    except EmptyDataError:
        input("Error: No data in DataFrame!")
    # Throw exception if table does not exist in DB.
    except UndefinedTable:
        input("Error: Table does not exist in database! Press enter to exit.")
