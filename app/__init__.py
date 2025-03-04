from flask import Flask
from app.routes import route_blueprints as rb


def create_flask_app(blueprints: list = rb):
    """Creates a Flask Application"""
    app = Flask(__name__)

    # register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint[1], url_prefix=blueprint[0])

    return app


# create the flask application
app = create_flask_app()
