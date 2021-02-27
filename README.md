# COVID-19-Tracker

A client for tracking the novel coronavirus, and various other tools for it.

## Project Goal

Build a web client to analyze and store global data for the SARS2-CoV-2 (COVID-19) pandemic, using various REST APIs. This started out as a simple console program to obtain, and analyze data. It has since evolved into a Flask application.

## Core Tools

- Python 3
- Pandas
- Requests
- Flask

## Running the Client Locally:

Required Technologies:

- Python 3

Steps:

- Clone repository.
- Open a terminal, and cd into repo.

*If you have GNU Make on your system, you can simply run `make init` from the project root to set up your dev environment.*

- Create, and activate a `venv`.
- Run `pip install -r requirements.txt` to install dependencies.
- Create a `.env` file in the root of the project directory, and add the following environment variables:
    - `ENV=dev`
    - `SECRET_KEY=(long, random string of characters)`
    - `ENGINE_STRING=SQL_Alchemy_Engine_String`
- Run `python app.py` to start the dev server.
- Navigate to `localhost:5000` in your web browser to preview the web client and data.

## Using CLI Tools

This client now also comes with some basic command line interface (CLI) tools, for users running the client locally. To use the CLI tools, activate your `venv`, run `cli.py` from the root of the project directory, and simply follow the prompts.

## Future Goals

- More statistics and data, especially for the U.S.
- Implement more complex data visualizations.
