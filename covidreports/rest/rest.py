from flask import Blueprint, jsonify, render_template
from requests import get
import pandas as pd


# Create a blueprint for the REST API
rest_bp = Blueprint(
    'api', 
    __name__,
    template_folder="templates",
    static_folder="static", 
)


"""
API endpoints for world data
"""

# All available data, for all countries 
world_summary = get("https://api.covid19api.com/summary").json()

# Route for API docs page
@rest_bp.route('/api/docs')
def api_docs():

    return render_template("apidocs.html", title="API Documentation")


@rest_bp.route('/api/world/summary', methods=["GET"])
def world_api_summary():

    df = pd.DataFrame(world_summary['Countries']).drop(["Premium"], axis=1)
    # Show totals for all columns
    total = df.sum(axis=0)
    # Convert the DataFrame to a dictionary
    df_dict = df.to_dict(orient='records')

    return jsonify(df_dict)


# Get historic data for a country
@rest_bp.route('/api/world/<string:country>/')
def country_api_history(country):

    # Define API endpoint, and fetch data
    endpoint = get(f'https://api.covid19api.com/total/country/{country}')
    data = endpoint.json()
    df = pd.DataFrame(data).sort_values(by="Date", ascending=False)
    df_dict = df.to_dict(orient="records")

    return jsonify(df_dict)


@rest_bp.route('/api/world/percentages/')
def world_api_percentages():

    df = pd.DataFrame(world_summary["Countries"])

    names = df["Country"]
    cases_percentages = round(df['TotalConfirmed'].div(
        world_summary['Global']['TotalConfirmed']), 2)
    deaths_percentages = round(df['TotalDeaths'].div(
        world_summary['Global']['TotalDeaths']), 2)
    recoveries_percentages = round(df['TotalRecovered'].div(
        world_summary['Global']['TotalRecovered']), 2)
    new_cases = round(df['NewConfirmed'].div(
        world_summary['Global']['NewConfirmed']), 2)
    new_deaths = round(df['NewDeaths'].div(
        world_summary['Global']['NewDeaths']), 2)
    new_recoveries = round(df['NewRecovered'].div(
        world_summary['Global']['NewRecovered']), 2)

    df_list = [names, cases_percentages, deaths_percentages,
               recoveries_percentages, new_cases, new_deaths, new_recoveries]
    merged_df = pd.concat(df_list, axis=1)
    merged_df_dict = merged_df.to_dict(orient='records')

    return jsonify(merged_df_dict)


"""
U.S. data API endpoints
"""

states_summary = get("https://api.covidtracking.com/v1/states/current.json").json()

# Current nationwide data for each state
@rest_bp.route('/api/us/summary/')
def us_api_summary():

    return jsonify(states_summary)


# History of COVID data for a specific state
@rest_bp.route('/api/us/state/<string:state>/')
def us_api_state(state):
    
    data = get(f"https://api.covidtracking.com/v1/states/{state}/daily.json").json()

    return jsonify(data)
