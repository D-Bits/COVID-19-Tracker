from dotenv import load_dotenv 
from os import getenv
from psycopg2 import connect
from sqlalchemy import create_engine
from requests import get
from flask import Flask, Blueprint


# Enable loading environment variables from .env file
load_dotenv()

# Define Blueprints for packages
world = Blueprint('world', __name__, template_folder="templates")

# Create a SQL Alchemy engine for the db
engine = create_engine(getenv("ENGINE_STRING"))

"""
Define API endpoints
"""
# All available data, for all countries 
summary = get("https://api.covid19api.com/summary")
summary_json = summary.json()
