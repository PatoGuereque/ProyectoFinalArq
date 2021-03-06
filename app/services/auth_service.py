from app.factory.user_factory import UserFactory
from ..extensions import db
from ..models import User


class Auth:
    ###################################
    # Single Responsibility Principle #
    ###################################
    def login(username, password):
        try:
            # fetch the user data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                return user, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    ###################################
    # Single Responsibility Principle #
    ###################################
    def register(username, password, email, preferences):
        user = User.query.filter_by(username=username).first()
        if not user:
            new_user = UserFactory.create_user(
                username, password, email, preferences)
            db.session.add(new_user)
            db.session.commit()
            return "True"
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409
