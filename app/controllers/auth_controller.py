from curses.ascii import isdigit
from flask import request
from flask import Blueprint

from app.utils.auth_util import validate_auth
from app.utils.preferences_util import validate_preferences
from ..services import Auth
from ..extensions import db

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/login', methods=["POST"])
def login():
    return validate_auth(request, lambda r, u: "success")

@auth_blueprint.route('/register', methods=["POST"])
def register():
    json_body = request.json

    if not "password" in json_body or not "password" in json_body or not "preferences" in json_body:
        return "Invalid body"

    username = json_body['username']
    password = json_body['password']
    email = json_body['email']
    preferences = json_body['preferences']

    if not validate_preferences(preferences):
        return "Invalid preference number", 400
    
    return Auth.register(username, password, email, preferences)

@auth_blueprint.route('/hello')
def hello_world():
    return "hello 2"


@auth_blueprint.route('/create')
def create_db():
    db.create_all()
    return "created?"