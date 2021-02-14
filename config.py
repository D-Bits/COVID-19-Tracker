"""
Module for global configs.
"""
from dotenv import load_dotenv 
from os import getenv
from sqlalchemy import create_engine
from requests import get


# Enable loading environment variables from .env file
load_dotenv()

# Create a SQL Alchemy engine for the db
engine = create_engine(getenv("ENGINE_STRING"))

