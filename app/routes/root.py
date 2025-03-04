from flask import Blueprint, render_template

root_blueprint = Blueprint('root_blueprint', __name__)


@root_blueprint.route("/")
def serve_landing():
    return render_template("index.html")


@root_blueprint.route("/docs")
def serve_docs():
    return render_template("docs.html")
