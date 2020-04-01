from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv
from config import summary_json
import pandas as pd


# Load environment variables from local .env file
load_dotenv() 

app = Flask(__name__)
# Load secret key
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

# Load environment type from environment var
ENV = getenv("ENV")

# Ensure debug is only on in development!
if ENV == 'dev':
    app.debug = True
else:
    app.debug = False


""" Routing logic """

# Routing/Controller logic for home page/summary data
@app.route('/')
@app.route('/home')
def index():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 98, 165, 171, 199, 219, 221])
    # Show totals for all columns
    total = cleaned_data.sum(axis=0)
    # Convert the DataFrame to a dictionary
    df_dict = cleaned_data.to_dict(orient='records')

    return render_template('index.html', data=df_dict, total=total)


# TODO: Build route and template for about page

# Route for cases page
@app.route('/cases')
def cases():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewConfirmed" and "TotalConfirmed", and countries names
    filtered_data = df.filter(items=['Country', 'NewConfirmed', 'TotalConfirmed'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])
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
    cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])
    # Sort TotalConfirmed in descending order
    sorted_data = df.sort_values(by='TotalDeaths', ascending=False)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')
    
    return render_template('deaths.html', data=df_dict)


# TODO: Implement routing logic for recoveries
@app.route('/recoveries')
def recoveries():

    df = pd.DataFrame(summary_json['Countries'])
    # Show only "NewDeaths" and "TotalDeaths", and countries names
    filtered_data = df.filter(items=['Country', 'NewRecovered', 'TotalRecovered'])
    # Drop redundant records obtained from API
    cleaned_data = filtered_data.drop([0, 93, 98, 165, 171, 199, 219, 221])
    # Sort TotalConfirmed in descending order
    sorted_data = df.sort_values(by='TotalRecovered', ascending=False)
    # Convert the DataFrame to a dictionary
    df_dict = sorted_data.to_dict(orient='records')
    
    return render_template('recoveries.html', data=df_dict)


if __name__ == "__main__":
    
    app.run() 