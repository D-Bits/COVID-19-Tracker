from dotenv import load_dotenv 
from os import getenv
from psycopg2 import connect
from sqlalchemy import create_engine
from requests import get
from flask import Flask


# Enable loading environment variables from .env file
load_dotenv()

app = Flask(__name__)
# Load secret key
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

# Load environment type from environment var
ENV = getenv("ENV")


"""
Define API endpoints
"""
# All available data, for all countries 
summary = get("https://api.covid19api.com/summary")
summary_json = summary.json()

