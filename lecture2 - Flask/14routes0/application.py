from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/david")
def david(): # it is a convention to name the function after the route
    return "Hello, David!"

@app.route("/amr")
def amr():
    return "Hello, Amr!"

@app.route("/amro")
def amro():
    return "Hello, Amroooo!"