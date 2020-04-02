from dotenv import load_dotenv 
from os import getenv
from psycopg2 import connect
from sqlalchemy import create_engine
from requests import get


# Enable loading environment variables from .env file
load_dotenv()

"""
Define API endpoints
"""
# All available data, for all countries 
summary = get("https://api.covid19api.com/summary")
summary_json = summary.json()

# All confirmed U.S. cases
usa_cases = get("https://api.covid19api.com/country/us/status/confirmed/live")
usa_json = usa_cases.json()