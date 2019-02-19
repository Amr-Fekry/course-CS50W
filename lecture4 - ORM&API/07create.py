import os

from flask import Flask, render_template, request
from models import *
# models is changed to 06models


# use this file as a flask app
app = Flask(__name__)
# link the app to database through the environment variable
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# tie the db defined in "models" with this flask app
db.init_app(app)

def main():
    db.create_all()
    # translates the the classes in "models" into SQL's CREATE TABLE syntax

if __name__ == "__main__":
	# needed to interact with the flask app on the commandline
    with app.app_context():
        main()
