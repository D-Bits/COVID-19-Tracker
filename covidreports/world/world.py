from flask import Blueprint, render_template, send_from_directory
from werkzeug.exceptions import NotFound, InternalServerError, ServiceUnavailable
from requests import get
from datetime import date, datetime, timedelta
from plotly.utils import PlotlyJSONEncoder
import plotly.express as px
import pandas as pd
import numpy as np
import json
import io


# Define Blueprint for world data
world_bp = Blueprint(
    "world",
    __name__,
    template_folder="templates",
    static_folder="static",
)

# All available data, for all countries
summary_json = get("https://api.covid19api.com/summary").json()

""" Routing logic """

# Route for home page/summary data
@world_bp.route("/")
def index():

    # Redirect to maintenance page if API is down
    if summary_json["Message"] == "Caching in progress":

        return render_template("maintenance.html", title="Maintenance Error")

    df = pd.DataFrame(summary_json["Countries"])
    # Show totals for all columns
    total = df.sum(axis=0)
    # Create a column to show a countries rank in no. of countries
    df["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
    # Convert the DataFrame to a dictionary
    df_dict = df.to_dict(orient="records")

    return render_template(
        "index.html",
        data=df_dict, 
        total=total,
        sorting="Country", 
        title="Home",
        length=len(df_dict)
    )


# Route for summary presented in different ordering
@world_bp.route("/<string:sorting>")
def world_data(sorting: str):

    # Redirect to maintenance page if API is down
    if summary_json["Message"] == "Caching in progress":

        return render_template("maintenance.html", title="Maintenance Error")

    df = pd.DataFrame(summary_json["Countries"])
    total = df.sum(axis=0)

    # Nested function for manipulating data
    def transform_data(sorting):  
        
        if sorting == "total_cases":
            sorted_data = df.sort_values(by="TotalConfirmed", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "new_cases":
            sorted_data = df.sort_values(by="NewConfirmed", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "total_deaths":
            df.sort_values(by="TotalDeaths", ascending=False)
            sorted_data = df.sort_values(by="TotalDeaths", ascending=False)
            # Create a column to show a countries rank in no. of deaths
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            return sorted_data.to_dict(orient="records")
        elif sorting == "new_deaths":
            sorted_data = df.sort_values(by="NewDeaths", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "total_recoveries":
            df.sort_values(by="TotalRecovered", ascending=False)
            sorted_data = df.sort_values(by="TotalRecovered", ascending=False)
            # Create a column to show a countries rank in no. of recoveries
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            return sorted_data.to_dict(orient="records")
        elif sorting == "new_recoveries":
            sorted_data = df.sort_values(by="NewRecovered", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "countries":
            df.sort_values(by="Country", ascending=False)
            return df.to_dict(orient="records")
        else:
            return render_template("404.html", title="404")


    return render_template(
        "index.html",
        data=transform_data(sorting),
        total=total,
        sorting=sorting,
        title=f"Global Data by {sorting.title()}"
    )


# Route for about page
@world_bp.route("/about")
def about():

    return render_template("about.html", title="About")


# Current case data for continents
@world_bp.route("/continents")
def continents():

    data = get("https://disease.sh/v3/covid-19/continents").json()
    df = (
        pd.DataFrame(data)
        .drop(["continentInfo", "countries", "updated"], axis=1)
        .sort_values(by="continent", ascending=True)
    )
    df_dict = df.to_dict(orient="records")

    return render_template("continents.html", data=df_dict, title="Continents")


# Route for non-COVID data about countries
@world_bp.route("/demographic/<string:sorting>")
def demographic(sorting):

    data = get("https://covid.ourworldindata.org/data/owid-covid-data.json").json()
    df = (
        pd.DataFrame(data)
        .drop(["data"])
        .transpose()
    )

    def transform_data(sorting):

        if sorting == "continent":
            sorted_data = df.sort_values(by="continent")
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "population":
            sorted_data = df.sort_values(by="population", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "population_density":
            sorted_data = df.sort_values(by="population_density", ascending=False)
            # Create a column to show a countries rank in no. of deaths
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            return sorted_data.to_dict(orient="records")
        elif sorting == "median_age":
            sorted_data = df.sort_values(by="median_age", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        elif sorting == "median_age":
            sorted_data = df.sort_values(by="median_age", ascending=False)
            # Create a column to show a countries rank in no. of cases
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            # Convert the DataFrame to a dictionary
            return sorted_data.to_dict(orient="records")
        else:
            sorted_data = df.sort_values(by="location", ascending=False)
            sorted_data["Rank"] = np.arange(start=1, stop=int(len(df)) + 1)
            return df.to_dict(orient="records")                

    return render_template("demographic.html", data=transform_data(sorting), title=f"Demographics by {sorting.title()}")


# Route to show how many cases, deaths, and recoveries a country had for each day, since first confirmed cases
# TODO: Format dates to strip out "T00:00:00Z"
@world_bp.route("/country/<string:country>")
def country_history(country: str):

    # Define API endpoint, and fetch data
    endpoint = get(f"https://api.covid19api.com/total/country/{country}")
    data = endpoint.json()
    # Redirect to 404 template if country doesn't exist
    if endpoint.status_code == 404:
        return render_template("404.html", title="404")
    df = pd.DataFrame(data)
    # Sort records from most recent cases to oldest cases
    sorted_data = df.sort_values("Date", ascending=False)
    df_dict = sorted_data.to_dict(orient="records")

    return render_template(
        "totals.html",
        data=df_dict,
        nation=country,
        title=f"{country.title()} COVID History",
    )


# Show percentage of case, deaths, and recoveries that countries constitute
@world_bp.route("/percentages")
def percentages():

    df = pd.DataFrame(summary_json["Countries"])

    names = df["Country"]
    cases_percentages = round(
        df["TotalConfirmed"].div(summary_json["Global"]["TotalConfirmed"]), 2
    )
    deaths_percentages = round(
        df["TotalDeaths"].div(summary_json["Global"]["TotalDeaths"]), 2
    )
    recoveries_percentages = round(
        df["TotalRecovered"].div(summary_json["Global"]["TotalRecovered"]), 2
    )
    new_cases = round(df["NewConfirmed"].div(summary_json["Global"]["NewConfirmed"]), 2)
    new_deaths = round(df["NewDeaths"].div(summary_json["Global"]["NewDeaths"]), 2)
    new_recoveries = round(
        df["NewRecovered"].div(summary_json["Global"]["NewRecovered"]), 2
    )

    df_list = [
        names,
        cases_percentages,
        deaths_percentages,
        recoveries_percentages,
        new_cases,
        new_deaths,
        new_recoveries,
    ]
    merged_df = pd.concat(df_list, axis=1)
    merged_df_dict = merged_df.to_dict(orient="records")

    return render_template(
        "percentages.html", data=merged_df_dict, title="Global Proportions"
    )


# Summary of global vaccination data
@world_bp.route("/vaccinations")
def vaccinations():

    # Fetch data from CSV on GitHub, and load into DataFrame
    data = get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv").content
    df = pd.read_csv(io.StringIO(data.decode('UTF-8')))
    # Data might be available for today for some countries
    yesterday = datetime.today() - timedelta(1) 
    yesterday_formatted = yesterday.strftime('%Y-%m-%d')
    current_data = df[df['date']==yesterday_formatted]
    df_dict = current_data.to_dict(orient="records") 

    return render_template(
        "world_vaccinations.html", 
        data=df_dict,
        title="World Vaccinations"
    )


# Vaccination history for a given country
@world_bp.route("/vaccinations/<string:country>")
def vaccination_history(country: str):

    # Fetch data from CSV on GitHub, and load into DataFrame
    data = get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv").content
    df = pd.read_csv(io.StringIO(data.decode('UTF-8')))
    nation = df[df['location']==country] 
    history = nation.sort_values(by="date", ascending=False)
    country_data = history.to_dict(orient="records")

    return render_template(
        "vaccination_history.html", 
        country=country,
        data=country_data,
        title=f"{country.title()} Vaccination History"
    )


# Route for showing line graph data for individual countries
@world_bp.route("/graphs/<string:country>")
def country_graphs(country: str):

    # Method to generate plots
    # "field" param can be equal to: "Confirmed", "Recovered", or "Deaths"
    def gen_plot(country, field):

        # Define API endpoint, and fetch data
        data = get(f"https://api.covid19api.com/total/country/{country}").json()
        df = pd.DataFrame(data)
        dates = df["Date"]
        case_type = df[field]
        # Create the plot, and convert it to a JSON object to iterate over in HTML
        graph_data = px.line(data_frame=df, x=dates, y=case_type)
        graph_JSON = json.dumps(graph_data, cls=PlotlyJSONEncoder)

        return graph_JSON

    return render_template(
        "country_graphs.html",
        nation=country,
        cases=gen_plot(country, "Confirmed"),
        deaths=gen_plot(country, "Deaths"),
        recoveries=gen_plot(country, "Recovered"),
        active=gen_plot(country, "Active"),
        title=f"{country.title()} Visualizations",
    )


# Download data from summary endpoint, and save to CSV
@world_bp.route(f"/dumps/summary_dump_{date.today()}.csv")
def download_summary():

    df = pd.DataFrame(summary_json["Countries"])
    # Order countries in alphabetical order
    ordered_df = df.sort_values("Country", ascending=True)
    # Dump the DataFrame to a CSV file, in a location of the user's choosing
    filename = f"./dumps/summary_dump_{date.today()}.csv"
    ordered_df.to_csv(filename, sep=",")

    # Download the data dump to user's client
    return send_from_directory("./dumps/", f"summary_dump_{date.today()}.csv")


"""
Error handling routes
"""
# 404 Handler
@world_bp.errorhandler(NotFound)
def not_found(e):

    return render_template("404.html", e=e, title="404"), 404


# 500 Handler
@world_bp.errorhandler(InternalServerError)
def server_error(e):

    return render_template("500.html", e=e, title="500"), 500

# 503 handler, in event API is down
@world_bp.errorhandler(ServiceUnavailable)
def api_unavailable(e):

    return render_template("maintenance.html", e=e, title="503"), 503
