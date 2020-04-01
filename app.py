from flask import Flask, render_template
from dotenv import load_dotenv
from os import getenv
from summary import sum_data
from config import summary_json
import pandas as pd

# Load environment variables from local .env file
load_dotenv() 

app = Flask(__name__)

# Load environment type from environment var
ENV = getenv("ENV")

# Ensure debug is only on in development!
if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

# TODO: Implement routing logic for all data sets/templates
""" Routing logic """

# Routing/Controller logic for home page/summary data
@app.route('/')
@app.route('/home')
def index():

    df = pd.DataFrame(summary_json['Countries'])
    # Drop redundant records obtained from API
    cleaned_data = df.drop([0, 93, 98, 165, 171, 199, 219, 221])
    # Convert the DataFrame to a dictionary
    df_dict = cleaned_data.to_dict(orient='records')

    return render_template('index.html', data=df_dict)



if __name__ == "__main__":
    
    app.run() 