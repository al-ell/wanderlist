import os
from flask import (
    Flask, flash, render_template, 
    request, redirect, url_for, session)
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal, User
from wanderlist.countries_api import get_countries
import json


@app.route("/")
def home():
    pics = ('wanderlist/static/images/')
    return render_template("index.html", pics=pics)



@app.route("/destinations/<country>", methods=["GET"])
def destinations(country):
    countries = get_countries()
    country_results = countries.get_countries(country=country)
    
    return render_template("destinations.html", countries=country_results)


@app.route("/trips")
def trips():
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    journal = list(Journal.query.order_by(Journal.id).all())
    return render_template("trips.html", trips=trips, journals=journal)


@app.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    if request.method == "POST":
        trips = Itineraries(
            trip_name = request.form.get("trip_name"),
            country_name = request.form.get("country_name"),
            to_go = bool(True if request.form.get("to_go") else False),
            created_by = session["user"]      
        )
        db.session.add(trips)
        db.session.commit()
        flash("Trip added!")
        return redirect(url_for("trips"))
               
    return render_template("add_trip.html")


@app.route("/edit_trip/<int:trip_id>", methods=["GET", "POST"])
def edit_trip(trip_id):
    trip = Itineraries.query.get_or_404(trip_id)
    if request.method == "POST":
        trip.trip_name = request.form.get("trip_name")
        trip.country_name = request.form.get("country_name")
        trip.to_go = bool(True if request.form.get("to_go") else False)
        trip.created_by = session["user"]
        db.session.commit()
        flash("Trip edited!")
        return redirect(url_for("trips"))
    return render_template("edit_trip.html", trip=trip)


@app.route("/delete_trip/<int:trip_id>")
def delete_trip(trip_id):
    trip = Itineraries.query.get_or_404(trip_id)
    db.session.delete(trip)
    db.session.commit()
    flash("Trip deleted!")
    # add defensive programming - pop up modal to query delete 
    return redirect(url_for("trips"))


@app.route("/journal")
def journal():
    journal = list(Journal.query.order_by(Journal.id).all())
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    return render_template("journal.html", journals=journal, trip=trips)


@app.route("/document", methods=["GET", "POST"])
def document():
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    if request.method == "POST":
        journal = Journal(
            trip_name = request.form.get("trip_name"),
            description = request.form.get("description"),
            rating = request.form.get("rating"),
            have_been = bool(True if request.form.get("have_been") else False),
            where = request.form.get("where"),
            when = request.form.get("when"),
            how = request.form.get("how"),
            itinerary_id = request.form.get("trip_id"),
            created_by = session["user"]      
        )
        db.session.add(journal)
        db.session.commit()
        flash("Journal entry added!")
        return redirect(url_for("journal"))
               
    return render_template("document.html", trips=trips)


@app.route("/edit_document/<int:journal_id>", methods=["GET", "POST"])
def edit_document(journal_id):
    journal = Journal.query.get_or_404(journal_id)
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    if request.method == "POST":
        journal.trip_name = request.form.get("trip_name")
        journal.description = request.form.get("description")
        journal.rating = request.form.get("rating")
        journal.have_been = bool(True if request.form.get("have_been") else False)
        journal.where = request.form.get("where")
        journal.when = request.form.get("when")
        journal.how = request.form.get("how")
        journal.itinerary_id = request.form.get("itinerary_id")
        journal.created_by = session["user"]
        db.session.commit()
        flash("Journal entry edited!")
        return redirect(url_for("journal"))
               
    return render_template("edit_document.html", journal=journal, trips=trips)


@app.route("/delete_document/<int:journal_id>")
def delete_document(journal_id):
    journal = Journal.query.get_or_404(journal_id)
    db.session.delete(journal)
    db.session.commit()
    flash("Journal entry deleted!")
    # add defensive programming - pop up modal to query delete 
    return redirect(url_for("journal"))