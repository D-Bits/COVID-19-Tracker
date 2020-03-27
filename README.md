# COVID-19-Tracker

A database for tracker the novel corona virus, and ETL tools for it.

## Project Goal
***

Build a database to store global data for the SARS2-CoV-2 (Covid 19) pandemic, using [Postman's APIs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest).

## Core Tools
***

- Python
- PostgreSQL
- Pandas
- Requests

## Project Setup
*** 

**How to setup the project locally on one's own machine:**

Required Technologies:

- Python 3
- PostgreSQL

Steps:

- Clone repository.
- Open a terminal, and cd into repo.
- Create, and activate a `venv`.
- Run `pip install -r requirements.txt` to install dependencies.
- Create a `.env` file, and add the necessary environment variables.
- Once you have created a db in Postgres, run the `CREATE TABLE` queries in the `tables.sql` file to build the db.
- Run the `main.py` file (with `venv` activated) from a terminal to load data into the database.

## Future Goals
***

- Automate updating the database with new data
- Build web client for database
- Implement data visualization