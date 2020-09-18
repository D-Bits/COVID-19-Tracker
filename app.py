from os import getenv
from dotenv import load_dotenv
from covidreports import create_app


# Load environment type from environment var
ENV = getenv("ENV")

app = create_app()

# Load secret key
app.config['SECRET_KEY'] = getenv("SECRET_KEY")


if __name__ == "__main__":

    # Ensure app.run() is only used in development.
    if ENV == "dev":
        app.run(debug=True, load_dotenv=True)
    else:
        pass
