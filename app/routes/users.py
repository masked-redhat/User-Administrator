from flask import Blueprint

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route("/")
def hello():
    return "pass"
