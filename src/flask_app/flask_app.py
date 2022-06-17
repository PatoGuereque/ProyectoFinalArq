from flask import Flask
from database import start_mappers

app = Flask(__name__)
start_mappers()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World!", 200