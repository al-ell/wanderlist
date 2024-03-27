import os
from flask_login import UserMixin
from wanderlist import app, db


class Itineraries(db.Model):
    # schema for the Itineraries model
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(30), nullable=False)
    country_name = db.Column(db.String(25), unique=True, nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    journal_entry = db.relationship("Journal", backref="itineraries", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in a string
        return self.trip_name


class Journal(db.Model):
    # schema for the Journal model
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    where = db.Column(db.Text, nullable=False)
    when = db.Column(db.Date, nullable=False)
    how = db.Column(db.String(30), nullable=False)
    created_by = db.Column(db.String(50), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
            self.id, self.trip_name


class User(db.Model, UserMixin):
    # schema for the user model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), db.ForeignKey("journal.id", ondelete="CASCADE"), unique=True, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    about = db.Column(db.Text(500), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.user
