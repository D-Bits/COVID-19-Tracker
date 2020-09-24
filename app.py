from os import getenv
from dotenv import load_dotenv
from covidreports import create_app
from covidreports.world.world import not_found, server_error


# Load environment type from environment var
ENV = getenv("ENV")

app = create_app()

# Load secret key
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

# Register error handlers
app.register_error_handler(404, not_found)
app.register_error_handler(500, server_error)


if __name__ == "__main__":

    # Ensure app.run() is only used in development.
    if ENV == "dev":
        app.run(debug=False, load_dotenv=True)
    else:
        pass
    