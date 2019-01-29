# import "session" to store user-specific data
from flask import Flask, render_template, request, session
# imoprt "Session" to control "session" 
from flask_session import Session

app = Flask(__name__)

# store the sessions server-side
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# empty global list to store data (drowback: accessible by all users)
notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", notes=notes)


# START HERE:
# a session is the concept of storing data that is accessible as long as the app (server) is running
# if the server in shutdown, however, data will be lost. BUT this can be solved using database storage

# notes list is a global variable, meaning it will be accessed by all server users.
# to make a user-specific session, we use falsk's "session" dictionary variable

"""
@app.route("/", methods=["GET", "POST"])
def index():
	# a session dict item is initialized inside the route function
	if session.get("notes") == None:
		session["notes"] = []

	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("index.html", notes=session["notes"])
"""
# flask's session identifies users browsers by storing cookies for each

