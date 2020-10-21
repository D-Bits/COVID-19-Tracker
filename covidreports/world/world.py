from flask import Blueprint, render_template, send_from_directory, jsonify
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError
from dotenv import load_dotenv
from requests import get
from os import getenv, remove
from datetime import date
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
import pandas as pd
import numpy as np
import json


# Define Blueprint for world data
world_bp = Blueprint(
    'world', 
    __name__, 
    template_folder="templates",
    static_folder="static",
)

# All available data, for all countries 
summary_json = get("https://api.covid19api.com/summary").json()

""" Routing logic """

# Route for home page/summary data
@world_bp.route('/')
def index():

    if summary_json['Message'] == "Caching in progress":

        return render_template("maintenance.html")

    df = pd.DataFrame(summary_json['Countries'])
    # Order countries in alphabetical order
    ordered_df = df.sort_values('Country', ascending=True)
    # Show totals for all columns
    total = df.sum(axis=0)
    # Convert the DataFrame to a dictionary
    df_dict = df.to_dict(orient='records')

    return render_template('index.html', data=df_dict, total=total, title="Home")


# Continent-specific data
@world_bp.route('/continents')
def continents():

    data = get("https://corona.lmao.ninja/v2/continents?yesterday=true&sort").json()
    df = pd.DataFrame(data)


# Route for about page
@world_bp.route('/about')
def about():

    return render_template('about.html', title="About")


# Route for cases page
@world_bp.route('/cases')
def cases():

    if summary_json['Message'] == "Caching in progress":

        return render_template("maintenance.html")

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewConfirmed', 'TotalConfirmed', 'Rank'])
    # Sort TotalConfirmed in descending order
    sorted_data = filtered_data.sort_values(by='TotalConfirmed', ascending=False)
    # Create a column to show a countries rank in no. of cases
    sorted_data['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('cases.html', data=df_dict, title="Global Cases")


# Route for deaths page
@world_bp.route('/deaths')
def deaths():

    if summary_json['Message'] == "Caching in progress":

        return render_template("maintenance.html")

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewDeaths', 'TotalDeaths'])
    # Sort TotalConfirmed in descending order
    sorted_data = filtered_data.sort_values(by='TotalDeaths', ascending=False)
    # Create a column to show a countries rank in no. of deaths
    sorted_data['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('deaths.html', data=df_dict, title="Global Deaths")


# Routing logic for recoveries
@world_bp.route('/recoveries')
def recoveries():

    if summary_json['Message'] == "Caching in progress":

        return render_template("maintenance.html")

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewDeaths" and "TotalDeaths", and countries names
    filtered_data = df.filter(
        items=['Country', 'NewRecovered', 'TotalRecovered'])
    # Sort TotalConfirmed in descending order
    sorted_data = filtered_data.sort_values(
        by='TotalRecovered', ascending=False)
    # Create a column to show a countries rank in no. of recoveries
    sorted_data['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('recoveries.html', data=df_dict, title="Global Recoveries")


# Route to show how many cases, deaths, and recoveries a country had for each day, since first confirmed cases
# TODO: Format dates to strip out "T00:00:00Z"
@world_bp.route('/country/<string:country>')
def country_history(country):

    # Define API endpoint, and fetch data
    endpoint = get(f'https://api.covid19api.com/total/country/{country}')
    data = endpoint.json()
    df = pd.DataFrame(data)
    # Sort records from most recent cases to oldest cases
    sorted_data = df.sort_values('Date', ascending=False)
    df_dict = sorted_data.to_dict(orient='records')

    return render_template('totals.html', data=df_dict, nation=country, title=f"{country} COVID History")


# Show percentage of case, deaths, and recoveries that countries constitute
@world_bp.route('/percentages')
def percentages():

    df = pd.DataFrame(summary_json["Countries"])

    names = df["Country"]
    cases_percentages = round(df['TotalConfirmed'].div(
        summary_json['Global']['TotalConfirmed']), 2)
    deaths_percentages = round(df['TotalDeaths'].div(
        summary_json['Global']['TotalDeaths']), 2)
    recoveries_percentages = round(df['TotalRecovered'].div(
        summary_json['Global']['TotalRecovered']), 2)
    new_cases = round(df['NewConfirmed'].div(
        summary_json['Global']['NewConfirmed']), 2)
    new_deaths = round(df['NewDeaths'].div(
        summary_json['Global']['NewDeaths']), 2)
    new_recoveries = round(df['NewRecovered'].div(
        summary_json['Global']['NewRecovered']), 2)

    df_list = [names, cases_percentages, deaths_percentages,
               recoveries_percentages, new_cases, new_deaths, new_recoveries]
    merged_df = pd.concat(df_list, axis=1)
    merged_df_dict = merged_df.to_dict(orient='records')

    return render_template("percentages.html", data=merged_df_dict, title="Global Proportions")


# Route for showing line graph data for individual countries
@world_bp.route("/graphs/<string:country>")
def country_graphs(country):

    # Method to generate plots
    # "field" param can be equal to: "Confirmed", "Recovered", or "Deaths"
    def gen_plot(country, field):

        # Define API endpoint, and fetch data
        endpoint = get(f'https://api.covid19api.com/total/country/{country}')
        data = endpoint.json()
        df = pd.DataFrame(data)
        dates = df["Date"]
        case_type = df[field]
        # Merge the "Date" and "Confirmed" fields into one df
        merged_df = pd.concat([dates, case_type], axis=1)
        # Create the plot, and convert it to a JSON object to iterate over in HTML
        graph_data = px.line(data_frame=df, x=df["Date"], y=df[field])
        graph_JSON = json.dumps(graph_data, cls=PlotlyJSONEncoder)

        return graph_JSON

    return render_template(
        "country_graphs.html",
        nation=country,
        cases=gen_plot(country, "Confirmed"),
        deaths=gen_plot(country, "Deaths"),
        recoveries=gen_plot(country, "Recovered"),
        active=gen_plot(country, "Active"),
        title=f"{country.title()} Visualizations"
    )


# Download data from summary endpoint, and save to CSV
@world_bp.route(f"/dumps/covid19_summary_{date.today()}.csv")
def download_summary():

    df = pd.DataFrame(summary_json['Countries'])

    # Order countries in alphabetical order
    ordered_df = df.sort_values('Country', ascending=True)
    # Dump the DataFrame to a CSV file, in a location of the user's choosing
    filename = f"/dumps/summary_dump_{date.today()}.csv"
    ordered_df.to_csv(filename, sep=",")

    # Download the data dump to user's client
    return send_from_directory('dumps/', f'summary_dump_{date.today()}.csv')
    remove(f"/dumps/summary_dump_{date.today()}.csv")


"""
Error handling routes
"""
# 404 Handler
@world_bp.errorhandler(NotFound)
def not_found(e):

    return render_template('404.html', e=e, title="404"), 404


# 500 Handler
@world_bp.errorhandler(InternalServerError)
def server_error(e):

    return render_template('500.html', e=e, title="500"), 500
