"""
A command line interface (CLI) to perform tasks for people
running the client locally.

Functionality:
1. Dump data to a CSV file.
"""
import pandas as pd
from datetime import datetime, date 
from config import summary_json


# Define user choices
choices = {
    0: "Exit Menu",
    1: "Dump summary data to CSV file",
}


# Dump summary data to a CSV file
def csv_dump(location):

    try: 
        df = pd.DataFrame(summary_json['Countries'])
        # Drop redundant records obtained from API
        cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
        # Order countries in alphabetical order
        ordered_df = cleaned_data.sort_values('Country', ascending=True)

        # Dump the DataFrame to a CSV file, in a location of the user's choosing
        ordered_df.to_csv(f"{location}/summary_dump_{date.today()}.csv", sep=",")

        print("DataFrame successfully dumped to:", location)

    except FileNotFoundError:

        print("That directory does not exist. Please try again.")


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