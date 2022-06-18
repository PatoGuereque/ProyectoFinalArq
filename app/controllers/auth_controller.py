from flask import request
from flask import Blueprint
from ..services import Auth
from ..extensions import db

auth_blueprint = Blueprint('/auth', __name__)

@auth_blueprint.route('/login', methods=["POST"])
def login():
    json_body = request.json

    if not "password" in json_body or not "password" in json_body:
        return "Invalid body"

    username = json_body['username']
    password = json_body['password']
    
    return Auth.login(username, password)

@auth_blueprint.route('/register', methods=["POST"])
def register():
    json_body = request.json

    if not "password" in json_body or not "password" in json_body:
        return "Invalid body"

    username = json_body['username']
    password = json_body['password']
    
    return Auth.register(username, password)

@auth_blueprint.route('/hello')
def hello_world():
    return "hello 2"


@auth_blueprint.route('/create')
def create_db():
    db.create_all()
    return "created?"