from flask import request
from flask import Blueprint
from app.services.preference_service import Preferences

from app.utils.auth_util import validate_auth

preference_blueprint = Blueprint('/preferences', __name__)

@preference_blueprint.route('/query', methods=["POST"])
def query():
    return validate_auth(request, Preferences.get_preferences)

@preference_blueprint.route('/update', methods=["POST"])
def update():
    return validate_auth(request, Preferences.update_preferences)