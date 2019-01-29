# passing variables to the html file

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world!"
    return render_template("index.html", headline=headline)

# headline=headline : the parameter is the one in the html file, and the value is the one in the python file
# it is a convention to give them the same name


@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

# the advantage of using render_template() is that we can create one html template and fill it with different content in different routes
