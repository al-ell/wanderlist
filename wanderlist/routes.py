import os
from flask import Flask, render_template
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal

import requests


class GetCountry():
    def __init__(self):
        self.my_api = "https://restcountries.com/v3.1/region/"
        self.country_api = "https://restcountries.com/v2/name/"


@app.route("/")
def home():
    pics = ('wanderlist/static/images/')
    return render_template("index.html", pics=pics)


@app.route("/journal_entries")
def journal_entries():
    
    return render_template("journal_entries.html")


@app.route("/destinations", methods=["GET"])
def destinations():
    
    return render_template("destinations.html")


@app.route("/my_trips")
def my_trips():

    return render_template("my_trips.html")


@app.route("/add_country", methods=["GET", "POST"])
def add_country():
        
    return render_template("add_countryy.html")

