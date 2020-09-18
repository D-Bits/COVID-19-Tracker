from dotenv import load_dotenv 
from os import getenv
from sqlalchemy import create_engine
from requests import get


# Enable loading environment variables from .env file
load_dotenv()

# Create a SQL Alchemy engine for the db
engine = create_engine(getenv("ENGINE_STRING"))

"""
Define API endpoints
"""
# All available data, for all countries 
summary = get("https://api.covid19api.com/summary")
summary_json = summary.json()
