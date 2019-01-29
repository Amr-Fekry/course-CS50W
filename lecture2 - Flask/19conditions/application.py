import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	# get the current date
    now = datetime.datetime.now()
    # assign True/False whether it is January 1 
    new_year = now.month == 1 and now.day == 1
    # pass the boolean value to index.html
    return render_template("index.html", new_year=new_year)
