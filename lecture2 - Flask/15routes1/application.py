from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

# turn a route into a template for a generalized set of routes

# allowing any route and passing it as a string variable
@app.route("/<string:name>") # anything typed after the slash will be saved as a string "name"
def hello(name): # pass name to the function
	# operate on the variable using python if needed
	name = name.capitalize()
	# return a formatted string
	
	nohtml = f"Hello, {name}!"
	# HTML can be used inside the app, but it should be separated if it is long
	html = f"<h1>Hello, {name}!</h1>"
	return nohtml + "\n" + html
