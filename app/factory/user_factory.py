from ..models import User


class UserFactory:

    ################
    # User Factory #
    ################
    def create_user(username, password, email, preferences) -> User:
        return User(
            username=username,
            password=password,
            email=email,
            preferences=preferences
        )
