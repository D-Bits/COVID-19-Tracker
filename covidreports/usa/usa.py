from flask import Blueprint, render_template
from requests import get
import pandas as pd 


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
    df_dict = sorted_df.to_dict(orient='records')

    return render_template("us_cases.html", data=df_dict)


# Show historical data for a specific state
@usa_bp.route('/us/<string:state>')
def state_history(state):

    data = get(f"https://api.covidtracking.com/v1/states/{state}/daily.json").json()
    df = pd.DataFrame(data)
    df_dict = df.to_dict(orient='records')

    return render_template("state_history.html", data=df_dict, state=state)
