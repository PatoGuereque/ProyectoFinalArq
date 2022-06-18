from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import MetaData

flask_bcrypt = Bcrypt()
db = SQLAlchemy()

def init_extensions(app):
    db.init_app(app)
    flask_bcrypt.init_app(app)
