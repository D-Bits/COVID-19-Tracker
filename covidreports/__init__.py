""" Application initialization """
from flask import Flask, current_app
from flask_assets import Environment, Bundle
from .world import world
from .usa import usa
from .rest import rest


# Initialize the app
def create_app():

    app = Flask(__name__)
    assets = Environment()
    assets.init_app(app)

    with app.app_context():

        # Register blueprints
        app.register_blueprint(world.world_bp)
        app.register_blueprint(usa.usa_bp)
        app.register_blueprint(rest.rest_bp)

        return app


def compile_static_asses(assets):

    assets.auto_build = True
