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


@app.route("/trips")
def trips():
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())

    return render_template("trips.html", trips=trips)


@app.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    if request.method == "POST":
        trips = Itineraries(
            trip_name=request.form.get("trip_name"),
            country_name=request.form.get("country_name"),
            to_go=bool(True if request.form.get("to_go") else False),
            created_by=request.form.get("created_by")      
        )
        db.session.add(trips)
        db.session.commit()
        return redirect(url_for("trips"))
               
    return render_template("add_trip.html")

