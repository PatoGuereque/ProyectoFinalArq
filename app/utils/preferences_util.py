from curses.ascii import isdigit

valid_preferences = ["1", "2", "3", "4", "5"]

def validate_preferences(preferences):
    validate_preferences = preferences.split(",")
    if len(validate_preferences) > 3:
        return False
    for preference in validate_preferences:
        if not isdigit(preference) or preference not in valid_preferences:
            return False
    return True