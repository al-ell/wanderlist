import os
from flask import render_template
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal

@app.route("/")
def home():
    pics = ('wanderlist/static/images/')
    return render_template("index.html", pics=pics)