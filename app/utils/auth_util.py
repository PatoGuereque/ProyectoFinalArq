from ..services import Auth

def validate_auth(request, handler):
    json_body = request.json

    if not "password" in json_body or not "password" in json_body:
        return "Invalid body"

    username = json_body['username']
    password = json_body['password']
    
    response_object, response_code = Auth.login(username, password)
    if response_code != 200:
        return response_object, response_code
    return handler(request, response_object)