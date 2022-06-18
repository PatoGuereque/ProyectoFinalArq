from ..extensions import db, flask_bcrypt

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password_hash = db.Column(db.String)
    favorites = db.Column(db.String)
    
    @property
    def password(self):
        # ISP principle
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return "<User '{}'>".format(self.username)