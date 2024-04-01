import os
from flask import (
    Flask, flash, render_template,
    request, redirect, url_for, session)
from wanderlist import app, db
from wanderlist.auth import routes
from wanderlist.models import Itineraries, Journal, User
import json


#  Route for homepage
@app.route("/")
def home():
    # To load background image
    pics = ('wanderlist/static/images/')
    #  Render index template
    return render_template("index.html", pics=pics)


#  Route for trips page
@app.route("/trips")
def trips():
    # filter through db entries to display current information
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    journals = list(Journal.query.order_by(Journal.id).all())
    #  Render trips template
    return render_template("trips.html", trips=trips, journals=journals)


# Route for add trip form
@app.route("/add_trip", methods=["GET", "POST"])
def add_trip():
    # Check if a user is logged in before allowing them to add a trip.
    if "user" not in session:
        # User feedback: must be logged in
        flash("You must be logged in to do that!")
        #  Return user to login page
        return redirect(url_for("auth.login"))
    # Check if trip name already taken
    trip_name = Itineraries.query.filter(
            Itineraries.trip_name == request.form.get("trip_name")).all()
    if trip_name:
        flash(
            # User feedback: trip name already exists in db
            "This Trip name is already taken. Please choose again.")
        #  Refresh add trip
        return redirect(url_for("add_trip"))
    #  If trip name is not taken add trip details to database.
    if request.method == "POST":
        trips = Itineraries(
            trip_name=request.form.get("trip_name"),
            country_name=request.form.get("country_name"),
            created_by=session["user"])
        #  Commit to database
        db.session.add(trips)
        db.session.commit()
        # User feedback: trip added
        flash("Trip added!")
        # Return user to trips page
        return redirect(url_for("trips"))
    # Render template for add trip page
    return render_template("add_trip.html")


# Route for edit trip
@app.route("/edit_trip/<int:trip_id>", methods=["GET", "POST"])
def edit_trip(trip_id):
    # Filter through trips to pre-populate on form load,
    # Return 404 error if query can't be completed
    trip = Itineraries.query.get_or_404(trip_id)
    # Check if user created the trip before allowing edit
    if "user" not in session or session["user"] != trip.created_by:
        flash("You can only edit your own trips!")
        return redirect(url_for("trips"))
    # Check if trip name already taken,
    # prevents allowing edit to be the same as another
    trip_name = Itineraries.query.filter(
            Itineraries.trip_name == request.form.get("trip_name")).all()
    if trip_name:
        flash(
            # User feedback: trip name already exists in db
            "This Trip name is already taken. Please choose again.")
        #  Reload add trip page
        return redirect(url_for("add_trip"))
    #  If trip name is not taken add trip details to database.
    if request.method == "POST":
        trip.trip_name = request.form.get("trip_name")
        trip.country_name = request.form.get("country_name")
        # Commit to db
        db.session.commit()
        # User feedback: trip updated in db
        flash("Trip edited!")
        # Reload trips page
        return redirect(url_for("trips"))
    #  Render template for edit trips
    return render_template("edit_trip.html", trip=trip)


# Route to delete trip
@app.route("/delete_trip/<int:trip_id>")
def delete_trip(trip_id):
    # Use trip id to query db
    # Return 404 error if query can't be completed
    trip = Itineraries.query.get_or_404(trip_id)
    # Check if user created the trip before allowing delete
    if "user" not in session or session["user"] != trip.created_by:
        # User feedback : can only delete own trips
        flash("You can only delete your own trips!")
        # Return user to trips page
        return redirect(url_for("trips"))
    # If they are the creator, delete the trip and commit changes
    db.session.delete(trip)
    db.session.commit()
    # User feedback : trip deleted
    flash("Trip deleted!")
    # Return user to trips page
    return redirect(url_for("trips"))


# Route for Journal
@app.route("/journal")
def journal():
    # Query db to retrieve journal and trips data
    journal = list(Journal.query.order_by(Journal.id).all())
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    #  Render template for journal page
    return render_template("journal.html", journals=journal, trip=trips)


# Route to add document to db
@app.route("/document", methods=["GET", "POST"])
def document():
    # Query db to retrieve trips data for selection in form
    trips = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    # Check that a user is logged in before allowing them to make journal entry
    if "user" not in session:
        # User feedback : must be logged in
        flash("You must be logged in to do that!")
        # Return user to login page
        return redirect(url_for("auth.login"))
    # Check if journal entry name already taken
    journal_name = Journal.query.filter(
            Journal.trip_name == request.form.get("trip_name")).all()
    if journal_name:
        flash(
            # User feedback : journal entry name already taken
            "This Journal Entry name is already taken. Please choose again.")
        # Refresh document page
        return redirect(url_for("document"))
    #  If trip name is not taken add trip details to database.
    if request.method == "POST":
        journal = Journal(
            trip_name=request.form.get("trip_name"),
            description=request.form.get("description"),
            where=request.form.get("where"),
            when=request.form.get("when"),
            how=request.form.get("how"),
            itinerary_id=request.form.get("trip_id"),
            created_by=session["user"])
        # Commit session to db
        db.session.add(journal)
        db.session.commit()
        # user feedback : journal entry added
        flash("Journal entry added!")
        # Return user to journal page
        return redirect(url_for("journal"))
    # Render template for document page
    return render_template("document.html", trips=trips)


# Route for edit document
@app.route("/edit_document/<int:journal_id>", methods=["GET", "POST"])
def edit_document(journal_id):
    # Query db to retrieve journal and trips data,
    # Return 404 error if query can't be completed
    journal = Journal.query.get_or_404(journal_id)
    trip = list(Itineraries.query.order_by(Itineraries.trip_name).all())
    # Check if user created the journal entry before allowing edit
    if "user" not in session or session["user"] != journal.created_by:
        # User feedback: cannot edit another users journal entries
        flash("You can only edit your own journal enteries!")
        # Return user to journals page
        return redirect(url_for("journal"))
    # Check if journal name already taken,
    # prevents allowing edit to be the same as another
    journal_name = Journal.query.filter(
            Journal.trip_name == request.form.get("trip_name")).all()
    if journal_name:
        flash(
            # User feedback: journal entry name already exists
            "This Journal Entry name is already taken. Please choose again.")
        # Refresh edit document page
        return redirect(url_for("edit_document"))
    #  If trip name is not taken add trip details to database
    if request.method == "POST":
        journal.trip_name = request.form.get("trip_name")
        journal.description = request.form.get("description")
        journal.where = request.form.get("where")
        journal.when = request.form.get("when")
        journal.how = request.form.get("how")
        journal.itinerary_id = request.form.get("itinerary_id")
        # Commit changes to db
        db.session.commit()
        # User feedback: journal entry added
        flash("Journal entry edited!")
        # Return user to journals page
        return redirect(url_for("journal"))
    # Render template for edit document
    return render_template("edit_document.html", journal=journal, trip=trip)


# Route for delete document
@app.route("/delete_document/<int:journal_id>")
def delete_document(journal_id):
    # Query db to retrieve journal and trips data,
    # Return 404 error if query can't be completed
    journal = Journal.query.get_or_404(journal_id)
    # Check if user created the journal entry before allowing delete
    if "user" not in session or session["user"] != journal.created_by:
        # User feedback: can only delete own journal entries
        flash("You can only delete your own journal enteries!")
        # Return user to journals page
        return redirect(url_for("journal"))
    # commit changes to db
    db.session.delete(journal)
    db.session.commit()
    # User feedback: journal entry deleted
    flash("Journal entry deleted!")
    # Return user to journals page
    return redirect(url_for("journal"))
