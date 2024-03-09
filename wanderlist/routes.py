from flask import render_template
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal

@app.route("/")
def home():
    return render_template("base.html")