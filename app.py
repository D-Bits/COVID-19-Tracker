from flask import Flask
from os import getenv
from world.config import world


# Load environment type from environment var
ENV = getenv("ENV")

app = Flask(__name__)

# Load secret key
app.config['SECRET_KEY'] = getenv("SECRET_KEY")

# Register blueprints
app.register_blueprint(world)

if __name__ == "__main__":

    # Ensure app.run() is only used in development.
    if ENV == "dev":
        app.run(debug=True, load_dotenv=True)
    else:
        pass
