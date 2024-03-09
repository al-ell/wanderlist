from wanderlist import db


class Itineraries(db.Model):
    # schema for the Journal model
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(25), unique=True, nullable=False)
    to_go = db.Column(db.Boolean, default=False, nullable=False)
    journal_entry = db.relationship("Journal", backref="itineraries", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.country_name


class Journal(db.Model):
    # schema for the Journal model
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    have_been = db.Column(db.Boolean, default=False, nullable=False)
    where = db.Column(db.Text, nullable=False)
    when = db.Column(db.Date, nullable=False)
    how = db.Column(db.String(30), nullable=False)
    itinerary_id = db.Column(db.Integer, db.ForeignKey("itineraries.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Journal: {1} | Been: {2}".format(
            self.id, self.trip_name, self.have_been
        )