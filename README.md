# COVID-19-Tracker

A database for tracker the novel corona virus, and ETL tools for it.

## Project Goal
***

Build a program, and a database, to analyze and store global data for the SARS2-CoV-2 (Covid 19) pandemic, using [Postman's APIs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest). This started out as a simple console program to obtain, and analyze data. It has since eveolved into a Flask application.

## Core Tools
***

- Python
- Pandas
- Requests
- Flask
- PostgreSQL

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
- Run `python app.py` to start the dev server.

## Future Goals
***

- Setup an automated pipeline to keep data up-to-date
- Build web client for database
- Implement data visualization