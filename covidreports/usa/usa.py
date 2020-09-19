from flask import Blueprint, render_template
from requests import get
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
import pandas as pd 
import numpy as np
import json


# Define Blueprint for U.S. specific data
usa_bp = Blueprint(
    'usa',
    __name__, 
    template_folder="templates",
    static_folder="static",
)

""" Routing logic """

# Summarize current U.S. data for COVID-19, per state/territory
@usa_bp.route('/us/summary')
def us_summary():

    data = get("https://api.covidtracking.com/v1/states/current.json").json()
    df = pd.DataFrame(data)
    df_dict = df.to_dict(orient='records')

    return render_template("us_summary.html", data=df_dict)


# Summary data, sorted by cases per state ascending 
@usa_bp.route('/us/cases')
def us_cases():

    data = get("https://api.covidtracking.com/v1/states/current.json").json()
    df = pd.DataFrame(data)
    # Order by positive cases ascending
    sorted_df = df.sort_values(by='positive', ascending=False)
    # Create a column to show a countries rank in no. of cases
    sorted_df['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    df_dict = sorted_df.to_dict(orient='records')

    return render_template("us_cases.html", data=df_dict)


# Summary data, sorted by deaths per state ascending
@usa_bp.route('/us/deaths')
def us_deaths():

    data = get("https://api.covidtracking.com/v1/states/current.json").json()
    df = pd.DataFrame(data)
    # Order by positive cases ascending
    sorted_df = df.sort_values(by='death', ascending=False)
    # Create a column to show a countries rank in no. of cases
    sorted_df['Rank'] = np.arange(start=1, stop=int(len(df))+1)
    df_dict = sorted_df.to_dict(orient='records')

    return render_template("us_deaths.html", data=df_dict)


# Show historical data for a specific state
@usa_bp.route('/us/<string:state>')
def state_history(state):

    data = get(f"https://api.covidtracking.com/v1/states/{state}/daily.json").json()
    df = pd.DataFrame(data)
    df_dict = df.to_dict(orient='records')

    return render_template("state_history.html", data=df_dict, state=state)


# Route for data visualizations for U.S. states
@usa_bp.route('/us/graphs/<string:state>')
def state_visualizations(state):

    # Method to generate plots
    # "field" param can be equal to: "Confirmed", "Recovered", or "Deaths"
    def gen_plot(state, field):

        data = get(f"https://api.covidtracking.com/v1/states/{state}/daily.json").json()
        df = pd.DataFrame(data)
        dates = df["date"]
        case_type = df[field]
        # Merge the "Date" and "Confirmed" fields into one df
        merged_df = pd.concat([dates, case_type], axis=1)
        graph_data = px.line(data_frame=df, x=df["date"], y=df[field])
        graph_JSON = json.dumps(graph_data, cls=PlotlyJSONEncoder)

        return graph_JSON

    return render_template(
        "state_graphs.html",
        state=state,
        cases=gen_plot(state, "positive"),
        deaths=gen_plot(state, "death"),
    )