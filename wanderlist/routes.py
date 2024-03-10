import os
from flask import Flask, render_template, request
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal
from api_class import GetCountry


@app.route("/")
def home():
    pics = ('wanderlist/static/images/')
    return render_template("index.html", pics=pics)


@app.route("/journal_entries")
def journal_entries():
    
    return render_template("journal_entries.html")


@app.route("/destinations", methods=["GET"])
def destinations():
    country = request.args.get("country")
    search = GetCountry()
    country_info = search.each_country(country=country)
    return render_template("destinations.html", country_list=country_info)


@app.route("/my_trips")
def my_trips():

    return render_template("my_trips.html")


@app.route("/add_trip")
def add_trip():

    return render_template("add_trip.html")


@app.route("/add_country", methods=["GET", "POST"])
def add_country():
    if request.method == "POST":
        category = Category(category_name=request.form.get("country_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("my_trips"))
    return render_template("add_countryy.html")

