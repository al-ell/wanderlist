import os
from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user)
from wanderlist import app, db, routes
from wanderlist.models import User, Journal, Itineraries
import json


# Blueprint created to allow seperate route for authentication.
auth = Blueprint("auth", __name__, url_prefix="/auth")


#  Use of login manager extension to allow user to login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


# https://flask-login.readthedocs.io/en/latest/#how-it-works
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# Route for registration
@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #  Check if user already exists in db, filter through existing users
        user = User.query.filter(
            # User.username == request.form.get("username").lower()).all()
            User.username == request.form.get("username").lower()).first()
        if user:
            flash(
                # User feedback: username already
                # registered form will not submit
                "This username is already registered. Please choose again.")
            return redirect(url_for("auth.register"))
        # If not registered, add form data to db
        register = User(
            username=request.form.get("username").lower(),
            name=request.form.get("name").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        # Commit to database
        db.session.add(register)
        db.session.commit()
        # User feedback
        flash("Registration Successful!")
        # send user to login once profile is made
        return redirect(url_for("home"))
    # Render register page
    return render_template("register.html")


# Route to login
@auth.route("/login", methods=["GET", "POST"])
def login():
    # Filter through users in db to retrieve user info
    if request.method == "POST":
        # Check if user already exists in the database
        exisiting_user = User.query.filter(
            User.username == request.form.get("username").lower()).all()
        #  If user exists check password is correct
        if exisiting_user:
            if check_password_hash(
                exisiting_user[0].password,
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                # Variable to target to hide register/login from session user
                session['logged_in'] = True
                # Take user to trips page after login
                return redirect(url_for("trips",
                                        username=session["user"]))
            # If user doesn't exist or username and/or passowrd is incorrect:
            else:
                # User feedback: invalid password, redirect to login page
                flash("Wrong Username and/ or Password")
                return redirect(url_for("auth.login"))
        else:
            # User feedback: username doesn't exist
            flash("Wrong Username and/ or Password")
    # Render login page
    return render_template("login.html")


# Route ot logout
@auth.route("/logout")
def logout():
    # Check if a user is logged in before allowing them to add a trip.
    if "user" not in session:
        # User feedback: must be logged in
        flash("You must be logged in to do that!")
        #  Return user to login page
        return redirect(url_for("auth.login"))
    #  User feedback: user logged out
    flash("You are logged out!")
    # logs user out
    session.pop("user")
    session['logged_out'] = True
    # Take user to homepage once logged out
    return redirect(url_for("home"))
