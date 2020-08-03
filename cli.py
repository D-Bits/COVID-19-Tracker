"""
A command line interface (CLI) to perform tasks for people
running the client locally.

Functionality:
1. Dump data to a CSV file.
"""
import pandas as pd
from datetime import datetime, date 
from pandas.errors import EmptyDataError
from psycopg2.errors import UndefinedTable
from config import summary_json, engine


# Define user choices
choices = {
    0: "Exit Menu",
    1: "Dump summary data to CSV file",
    2: "Write the summary data to a Postgres db.",
}

# Dump summary data to a CSV file, in a directory of the user's choosing
def csv_dump(location):

    try: 
        df = pd.DataFrame(summary_json['Countries'])
        # Drop redundant records obtained from API
        cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
        # Order countries in alphabetical order
        ordered_df = cleaned_data.sort_values('Country', ascending=True)

        # Dump the DataFrame to a CSV file, in a location of the user's choosing
        ordered_df.to_csv(f"{location}/summary_dump_{date.today()}.csv", sep=",")

        print('DataFrame successfully dumped to:', location, f'as "summary_dump_{date.today()}.csv"')

    except FileNotFoundError:

        print("ERROR: That directory does not exist. Please try again.")

    except EmptyDataError:

        print("ERROR: DataFrame is empty.")


"""
Params:
- data_src = the API endpoint
- table = the db table the data is to be written to
- dropped_records = a list of row numbers to be dropped prior to ingestion, 
                    or 0 if no records are to be dropped.
"""
def data_etl(table):

    try:
        # Load API JSON data into DataFrame
        df = pd.DataFrame(summary_json)
        # Drop slug field from DataFrame
        cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
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


def main():

    # Display the user's options, and prompt them to make a choice
    for key, val in choices.items():

        print(key, val)
    
    user_choice = int(input("Enter an int, based on the above options: "))

    if user_choice == 0:
        pass
    elif user_choice == 1:
        # Prompt the user to input the dir where they want their CSV dump saved
        user_dir = input("Enter the full path of the directory that you want your data saved in: ")
        csv_dump(user_dir)
    else:
        print("Invalid value entered. Try again, please.")
        main()


main()