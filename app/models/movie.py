from ..extensions import db

class Movie(db.Model):
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True)
    preference_key = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)
    create_time = db.Column(db.TIMESTAMP(timezone=True), index=True)
