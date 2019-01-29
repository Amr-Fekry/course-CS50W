# the main file of a flask app is generally called "application.py" 

# import "Flask" class that creates a flask web server
from flask import Flask

# make a flask server out of this file and refer to it as "app"
app = Flask(__name__)

# the route is the part of the url that determines the page requested
# the slash represents the default page "index.html"
@app.route("/") # decorator
def index():
    return "Hello, world!"

# decorators tie the function immediately below it to the even of requesting a specific route
