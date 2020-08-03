from flask import Flask, render_template, send_from_directory
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError
from dotenv import load_dotenv
from requests import get
from os import getenv, remove
from datetime import date
from config import summary_json, app, ENV
from bokeh.plotting import figure, output_file
from bokeh.models import ColumnDataSource
from bokeh.embed import components
import pandas as pd
import numpy as np


""" 
Routing logic 
"""

# Route for home page/summary data 
@app.route('/')
def index():

    df = pd.DataFrame(summary_json['Countries'])
    # Order countries in alphabetical order
    ordered_df = df.sort_values('Country', ascending=True)
    # Show totals for all columns
    total = df.sum(axis=0)
    # Convert the DataFrame to a dictionary
    df_dict = df.to_dict(orient='records')

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
    filtered_data = df.filter(items=['Country', 'NewConfirmed', 'TotalConfirmed', 'Rank'])
    # Sort TotalConfirmed in descending order
    sorted_data = filtered_data.sort_values(by='TotalConfirmed', ascending=False)
    # Create a column to show a countries rank in no. of cases
    sorted_data['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('cases.html', data=df_dict)


# Route for deaths page
@app.route('/deaths')
def deaths():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewDeaths', 'TotalDeaths'])
    # Sort TotalConfirmed in descending order
    sorted_data = filtered_data.sort_values(by='TotalDeaths', ascending=False)
    # Create a column to show a countries rank in no. of deaths
    sorted_data['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('deaths.html', data=df_dict)


# Routing logic for recoveries
@app.route('/recoveries')
def recoveries():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewDeaths" and "TotalDeaths", and countries names
    filtered_data = df.filter(items=['Country', 'NewRecovered', 'TotalRecovered'])
    # Sort TotalConfirmed in descending order
    sorted_data = filtered_data.sort_values(by='TotalRecovered', ascending=False)
    # Create a column to show a countries rank in no. of recoveries
    sorted_data['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('recoveries.html', data=df_dict)


# TODO: Format dates to strip out "T00:00:00Z"
# Route to show data in a specific country, by date
@app.route('/country/<string:country>')
def country_cases(country):

    # Define API endpoint, and fetch data
    endpoint = get(f'https://api.covid19api.com/live/country/{country}')
    # TODO: Add error handling for 404s here
    data = endpoint.json()
    df = pd.DataFrame(data).astype({"Date": "datetime64[ns]"})
    # Sort records from most recent cases to oldest cases
    sorted_data = df.sort_values('Date', ascending=False)
    df_dict = sorted_data.to_dict(orient='records')
    
    return render_template('country.html', data=df_dict, nation=country)


# Route to show how many cases, deaths, and recoveries a country had for each day, since first confirmed cases
# TODO: Format dates to strip out "T00:00:00Z"
@app.route('/totals/<string:country>')
def country_history(country):

    # Define API endpoint, and fetch data
    endpoint = get(f'https://api.covid19api.com/total/country/{country}')
    data = endpoint.json()
    df = pd.DataFrame(data)
    # Sort records from most recent cases to oldest cases
    sorted_data = df.sort_values('Date', ascending=False)
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('totals.html', data=df_dict, nation=country)


# Show percentage of case, deaths, and recoveries that countries constitute
@app.route('/percentages')
def percentages():

    countries = pd.DataFrame(summary_json["Countries"])

    names = countries["Country"]
    cases_percentages = round(countries['TotalConfirmed'].div(summary_json['Global']['TotalConfirmed']), 2)
    deaths_percentages = round(countries['TotalDeaths'].div(summary_json['Global']['TotalDeaths']), 2)
    recoveries_percentages = round(countries['TotalRecovered'].div(summary_json['Global']['TotalRecovered']), 2)
    new_cases = round(countries['NewConfirmed'].div(summary_json['Global']['NewConfirmed']), 2)
    new_deaths = round(countries['NewDeaths'].div(summary_json['Global']['NewDeaths']), 2)
    new_recoveries = round(countries['NewRecovered'].div(summary_json['Global']['NewRecovered']), 2)

    df_list = [names, cases_percentages, deaths_percentages, recoveries_percentages, new_cases, new_deaths, new_recoveries]
    merged_df = pd.concat(df_list, axis=1)
    merged_df_dict = merged_df.to_dict(orient='records')

    return render_template("percentages.html", data=merged_df_dict)


# Download data from summary endpoint, and save to CSV
@app.route(f"/dumps/covid19_summary_{date.today()}.csv")
def download_summary():

    df = pd.DataFrame(summary_json['Countries'])

    # Order countries in alphabetical order
    ordered_df = df.sort_values('Country', ascending=True)
    # Dump the DataFrame to a CSV file, in a location of the user's choosing
    filename = f"dumps/summary_dump_{date.today()}.csv"
    ordered_df.to_csv(filename, sep=",")

    # Download the data dump to user's client
    return send_from_directory('dumps/', f'summary_dump_{date.today()}.csv', )
    remove(f'dumps/summary_dump_{date.today()}.csv')


"""
Error handling routes
"""
# 404 Handler
@app.errorhandler(404)
def not_found(error):

    return render_template('404.html'), 404


# 500 Handler
@app.errorhandler(500)
def server_error(error):

    return render_template('500.html'), 500


if __name__ == "__main__":

    # Ensure app.run() is only used in development.
    if ENV == "dev":
        app.run(debug=True, load_dotenv=True)
    else:
        pass
