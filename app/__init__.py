from flask import Flask, url_for

from .config import Config
from .controllers.auth_controller import auth_blueprint
from .controllers.preferences_controller import preference_blueprint
from .controllers.movies_constroller import movies_blueprint
from .extensions import init_extensions


def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(preference_blueprint, url_prefix='/preferences')
    app.register_blueprint(movies_blueprint, url_prefix='/movies')

    app.config.from_object(Config)
    init_extensions(app)
    return app