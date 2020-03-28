from dotenv import load_dotenv 
from os import getenv
from psycopg2 import connect
from sqlalchemy import create_engine
from requests import get


# Enable loading environment variables from .env file
load_dotenv()

# Load db credentials from environment vars
db_host = getenv('DB_HOST')
db_name = getenv("DB_NAME")
db_user = getenv('DB_USER')
db_pass = getenv('DB_PASS')
db_port = getenv('DB_PORT')

# Establish db connection
db_connection = connect(database=db_name, host=db_host, user=db_user, password=db_pass)

# Create a SQLAlchemy engine to execute queries
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/covid19")

"""
Define API endpoints
"""
# All available data, for all countries 
summary = get("https://api.covid19api.com/summary")
summary_json = summary.json()

# All confirmed U.S. cases
usa_cases = get("https://api.covid19api.com/country/us/status/confirmed/live")
usa_json = usa_cases.json()