"""Main app"""

from flask import Blueprint, jsonify

from app.config import get_config as config

bp: Blueprint = Blueprint(
    name="main", import_name=__name__, url_prefix="/", template_folder="templates"
)


@bp.route("/", methods=["GET"])
def main_route():
    """This is the main (base) route of the app"""
    return jsonify({"message": f"Hello World your on {config.BASE_URL}!"})
