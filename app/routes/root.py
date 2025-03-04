from flask import Blueprint, render_template

root_blueprint = Blueprint('root_blueprint', __name__)


@root_blueprint.route("/")
def serve_html():
    return render_template("index.html")
