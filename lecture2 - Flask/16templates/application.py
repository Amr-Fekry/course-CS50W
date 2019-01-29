# imoprt render_template() so you can connect html files to the app
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# html files should be located in a folder called templates in the cwd
