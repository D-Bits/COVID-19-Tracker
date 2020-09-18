from flask import Flask
from os import getenv
from dotenv import load_dotenv
from world import world_blueprint


# Load environment type from environment var
ENV = getenv("ENV")

app = Flask(__name__)

# Load secret key
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

# Register blueprints
app.register_blueprint(world_blueprint)

if __name__ == "__main__":

    # Ensure app.run() is only used in development.
    if ENV == "dev":
        app.run(debug=True, load_dotenv=True)
    else:
        pass
