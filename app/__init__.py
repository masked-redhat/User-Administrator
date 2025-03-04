from flask import Flask
from mongoengine import connect, disconnect
from app.routes import route_blueprints as rb
from app.config import Config


def create_flask_app(blueprints: list = rb):
    """Creates a Flask Application"""
    app = Flask(__name__)

    # register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint[1], url_prefix=blueprint[0])

    return app


def connect_db():
    """Connects to the database with env specified keys"""
    connect(Config.DATABASE.DB,
            host=Config.DATABASE.HOST,
            port=Config.DATABASE.PORT,
            alias=Config.DATABASE.CONN)
    print("Mongo database connected!")


def shutdown_db():
    """Disconnectes the mongo connection"""
    disconnect(Config.DATABASE.CONN)
    print("Mongo database shutdown")
