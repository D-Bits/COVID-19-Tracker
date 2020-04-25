from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from requests import get
from os import getenv, remove
from datetime import date
from config import summary_json, app, ENV
import pandas as pd


# Load environment variables from local .env file
load_dotenv() 


""" Routing logic """

# Routing/Controller logic for home page/summary data
@app.route('/')
@app.route('/home')
def index():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
    # Order countries in alphabetical order
    ordered_df = cleaned_data.sort_values('Country', ascending=True)
    # Show totals for all columns
    total = cleaned_data.sum(axis=0)
    # Convert the DataFrame to a dictionary
    df_dict = ordered_df.to_dict(orient='records')

    return render_template('index.html', data=df_dict, total=total)


# Route for about page
@app.route('/about')
def about():

    return render_template('about.html')


# Route for cases page
@app.route('/cases')
def cases():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewConfirmed', 'TotalConfirmed'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
    # Sort TotalConfirmed in descending order
    sorted_data = df.sort_values(by='TotalConfirmed', ascending=False)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')
    
    return render_template('cases.html', data=df_dict)


# Route for deaths page 
@app.route('/deaths')
def deaths():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewDeaths', 'TotalDeaths'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
    # Sort TotalConfirmed in descending order
    sorted_data = df.sort_values(by='TotalDeaths', ascending=False)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')
    
    return render_template('deaths.html', data=df_dict)


# Routing logic for recoveries
@app.route('/recoveries')
def recoveries():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewDeaths" and "TotalDeaths", and countries names
    filtered_data = df.filter(items=['Country', 'NewRecovered', 'TotalRecovered'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
    # Sort TotalConfirmed in descending order
    sorted_data = df.sort_values(by='TotalRecovered', ascending=False)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')
    
    return render_template('recoveries.html', data=df_dict)


# Route for countries with no data/0 cases 
@app.route('/null')
def no_data():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "TotalConfirmed" and "NewConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'TotalConfirmed', 'NewConfirmed'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
    # Show only countries with 0 reported cases
    null_countries = cleaned_data.loc[cleaned_data['TotalConfirmed'] == 0]
    # Order countries in alphabetical order
    ordered_df = null_countries.sort_values('Country', ascending=True)
    # Convert the DataFrame to a dictionary
    df_dict = ordered_df.to_dict(orient='records')
    
    return render_template('null_countries.html', data=df_dict)


# Route to show cases in a specific country
@app.route('/<string:country>')
def country_cases(country):

    # Define API endpoint, and fetch data
    endpoint = get(f'https://api.covid19api.com/country/{country}/status/confirmed/live')
    data = endpoint.json()
    df = pd.DataFrame(data)
    # Remove records with no cases
    cleaned_data = df.loc[df['Cases'] > 0]
    # Sort records from most recent cases to oldest cases
    sorted_data = cleaned_data.sort_values('Date', ascending=False)
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('country.html', data=df_dict, nation=country)


# Download data from summary endpoint, and save to CSV
@app.route(f"/dumps/covid19_summary_{date.today()}.csv")
def download_summary():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 101, 125, 168, 169, 170, 171, 172, 175, 194, 199, 205, 224])
    # Order countries in alphabetical order
    ordered_df = cleaned_data.sort_values('Country', ascending=True)
    # Dump the DataFrame to a CSV file, in a location of the user's choosing
    filename = f"dumps/summary_dump_{date.today()}.csv"
    csv_dump = ordered_df.to_csv(filename, sep=",")

    # Download the data dump to user's client
    return send_from_directory('dumps/', f'summary_dump_{date.today()}.csv')
    remove(f'dumps/summary_dump_{date.today()}.csv')
    

"""
Error handling routes
"""
# 404 Handler
@app.errorhandler(404)
def not_found(error):

    return render_template('404.html')


# 500 Handler
@app.errorhandler(500)
def five_hundred_error(error):

    return render_template('500.html')


# 503 Handler
@app.errorhandler(503)
def five_oh_three_error(error):

    return render_template('503.html')
    

# TODO: Add tools for file downloads


if __name__ == "__main__":
    
    # Ensure app.run() is only used in development.
    if ENV == "dev":
        app.run(debug=True)
    else:
        pass 