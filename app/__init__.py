from flask import Flask
from mongoengine import connect, disconnect
from app.routes import route_blueprints as rb
from env import DatabaseEnv as db


def create_flask_app(blueprints: list = rb):
    """Creates a Flask Application"""
    app = Flask(__name__)

    # register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint[1], url_prefix=blueprint[0])

    return app


def connect_db():
    """Connects to the database with env specified keys"""
    connect(db.DB, host=db.HOST, port=db.PORT, alias=db.CONN)
    print("Mongo database connected!")


def shutdown_db():
    """Disconnectes the mongo connection"""
    disconnect(db.CONN)
    print("Mongo database shutdown")
