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