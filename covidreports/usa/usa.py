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

# Summary of current data for all states
states_summary = get("https://disease.sh/v3/covid-19/nyt/states?lastdays=1").json()


# Summarize current U.S. data for COVID-19, per state/territory
@usa_bp.route('/us/summary/<string:sorting>')
def us_summary(sorting: str):

    df = pd.DataFrame(states_summary)

    def transform_data(sorting):

        if sorting == "cases":
            sorted_data = df.sort_values(by="cases", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "deaths":
            sorted_data = df.sort_values(by="deaths", ascending=False)
            # Create a column to show a countries rank in no. of deaths
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        else:
            sorted_data = df.sort_values(by="state", ascending=True)
            # Create a column to show a countries rank in no. of recoveries
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")

    return render_template(
        "us_summary.html", 
        data=transform_data(sorting), 
        title=f"U.S. Summary by {sorting.title()}"
    )

'''
# Summary data, sorted by cases per state ascending 
@usa_bp.route('/us/cases')
def us_cases():

    df = pd.DataFrame(states_summary)
    # Order by positive cases ascending
    sorted_df = df.sort_values(by='positive', ascending=False)
    # Create a column to show a countries rank in no. of cases
    sorted_df['Rank'] = np.arange(start=1, stop=int(len(df)) + 1)
    df_dict = sorted_df.to_dict(orient='records')

    return render_template("us_cases.html", data=df_dict, title="U.S. Cases")


# Summary data, sorted by deaths per state ascending
@usa_bp.route('/us/deaths')
def us_deaths():

    df = pd.DataFrame(states_summary)
    # Order by positive cases ascending
    sorted_df = df.sort_values(by='death', ascending=False)
    # Create a column to show a countries rank in no. of cases
    sorted_df['Rank'] = np.arange(start=1, stop=int(len(df)) + 1)
    df_dict = sorted_df.to_dict(orient='records')

    return render_template("us_deaths.html", data=df_dict, title="U.S. Deaths")
'''

# Show historical data for a specific state
@usa_bp.route('/us/<string:state>')
def state_history(state):

    data = get(f"https://disease.sh/v3/covid-19/nyt/states/{state}?lastdays=all").json()
    df = pd.DataFrame(data)
    sorted_values = df.sort_values(by="date", ascending=False)
    df_dict = sorted_values.to_dict(orient='records')

    return render_template(
        "state_history.html", 
        data=df_dict, 
        state=state, 
        title=f"U.S.-{state} COVID History"
    )


# Route for data visualizations for U.S. states
@usa_bp.route('/us/graphs/<string:state>')
def state_visualizations(state):

    # Method to generate plots
    # "field" param can be equal to: "Confirmed", "Recovered", or "Deaths"
    def gen_plot(state, field):

        data = get(f"https://disease.sh/v3/covid-19/nyt/states/{state}?lastdays=all").json()
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
        cases=gen_plot(state, "cases"),
        deaths=gen_plot(state, "deaths"),
        title=f"{state} Visualizations"
    )


# Get current data for all U.S. counties
@usa_bp.route('/us/counties/<string:sorting>')
def counties(sorting):

    data = get("https://disease.sh/v3/covid-19/nyt/counties?lastdays=1").json()
    df = pd.DataFrame(data)

    # Nested function for sorting data
    def transform_data(sorting):

        if sorting == "cases":
            sorted_data = df.sort_values(by="cases", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "deaths":
            sorted_data = df.sort_values(by="deaths", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "county":
            sorted_data = df.sort_values(by="county", ascending=True)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "state":
            sorted_data = df.sort_values(by="state", ascending=True)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        else:
            pass

    return render_template("counties.html", data=transform_data(sorting), title=f"U.S. Counties by {sorting.title()}")
