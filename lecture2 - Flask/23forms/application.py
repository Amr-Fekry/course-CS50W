# import "request" to access form info
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
	name = request.form.get("name")
	return render_template("hello.html", name=name)

"""
"/hello" route is currently accepting "post" requests only
it is expecting info from the form when it is called

to accept both methods

@app.route("/hello", methods=["GET", "POST"])
def hello():
	if request.method == "GET":
		return "Please submit the form instead."
	else:
    	name = request.form.get("name")
    	return render_template("hello.html", name=name)

"""