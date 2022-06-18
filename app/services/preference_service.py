from app.utils.preferences_util import validate_preferences
from ..models import User
from ..extensions import db

class Preferences:
    def get_preferences(request, user: User):
        return user.preferences

    def update_preferences(request, user: User):
        json_body = request.json
        if not "preferences" in json_body:
            return "Invalid body"

        preferences = json_body['preferences']
        if not validate_preferences(preferences):
            return "Invalid preference number", 400
        
        user.preferences = preferences
        db.session.commit()

        return user.preferences