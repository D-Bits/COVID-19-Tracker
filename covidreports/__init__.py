""" Application initialization """
from flask import Flask
from requests import get
from .world import world


# Initialize the app
def create_app():

    app = Flask(__name__)

    with app.app_context():

        # Register blueprints
        app.register_blueprint(world.world_bp)

        return app