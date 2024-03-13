import os
from flask import Flask, render_template, request, redirect, url_for
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal
from wanderlist.countries_api import get_countries
import json


@app.route("/")
def home():
    pics = ('wanderlist/static/images/')
    return render_template("index.html", pics=pics)


@app.route("/journal_entries")
def journal_entries():
    
    return render_template("journal_entries.html")


@app.route("/destinations/<country>", methods=["GET"])
def destinations(country):
    countries = get_countries()
    country_results = countries.get_countries(country=country)
    
    return render_template("destinations.html", countries=country_results)


@app.route("/my_trips")
def my_trips():


    return render_template("my_trips.html")


@app.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    if request == "POST":
        trip = Itineraries(trip_name=request.form.get("trip_name"))
        db.session.add(trip)
        db.session.commit()
        return redirect(url_for("my_trips"))
               
    return render_template("add_trip.html")

