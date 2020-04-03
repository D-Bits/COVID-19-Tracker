# COVID-19-Tracker

A client for tracking the novel corona virus, and various other tools for it.

## Project Goal
***

Build a program, and a database, to analyze and store global data for the SARS2-CoV-2 (Covid 19) pandemic, using [Postman's APIs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest). This started out as a simple console program to obtain, and analyze data. It has since eveolved into a Flask application.

## Core Tools
***

- Python 3
- Pandas
- Requests
- Flask

## Project Setup
*** 

**Running the Client Locally:**

Required Technologies:

- Python 3

Steps:

- Clone repository.
- Open a terminal, and cd into repo.
- Create, and activate a `venv`.
- Run `pip install -r requirements.txt` to install dependencies.
- Create a `.env` file in the root of the project directory, and add the following environment variables:
    - `ENV=dev`
    - `SECRET_KEY=(long, random string of characters)`
- Run `python app.py` to start the dev server.
- Navigate to `localhost:5000` in your web browser to preview the web client and data.

## Future Goals
***

- Add CLI tools for users running the client locally.
- More statistics and data
- Implement data visualization.
