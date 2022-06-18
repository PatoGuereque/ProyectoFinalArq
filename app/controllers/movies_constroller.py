from flask import request
from flask import Blueprint
from app.services.movie_service import MovieService
from app.utils.auth_util import validate_auth

movies_blueprint = Blueprint('/movies', __name__)

@movies_blueprint.route('/search', methods=["POST"])
def search():
    return validate_auth(request, MovieService.query_movies)