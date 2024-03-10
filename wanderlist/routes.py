import os
from flask import Flask, render_template
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal
import requests
import json


@app.route("/")
def home():
    pics = ('wanderlist/static/images/')
    return render_template("index.html", pics=pics)


@app.route("/journal_entries")
def journal_entries():
    
    return render_template("journal_entries.html")


@app.route("/destinations", methods=["GET"])
def destinations():
    req = requests.get("https://restcountries.com/v3.1/all")
    data = json.loads(req.content)
    return render_template("destinations.html", data=data)