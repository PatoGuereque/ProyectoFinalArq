from flask import Flask, url_for

from .config import Config
from .controllers.auth_controller import auth_blueprint
from .extensions import init_extensions


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    app.config.from_object(Config)
    init_extensions(app)
    return app