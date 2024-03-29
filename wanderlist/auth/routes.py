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
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
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


auth = Blueprint("auth", __name__, url_prefix="/auth")


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


# https://flask-login.readthedocs.io/en/latest/#how-it-works
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #  Check if user already registered
        user = User.query.filter(
            User.username == request.form.get("username").lower()).all()
        if user:
            flash(
                "This username is already registered. Please choose again.")
            return redirect(url_for("auth.register"))
        # If not registered, add form data to db
        register = User(
            username=request.form.get("username").lower(),
            name=request.form.get("name").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        db.session.add(register)
        db.session.commit()
        flash("Registration Successful!")
        # send user to login once profile is made
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if user already exists in the database
        exisiting_user = User.query.filter(
            User.username == request.form.get("username").lower()).all()

        if exisiting_user:
            if check_password_hash(
                exisiting_user[0].password,
                    request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for("auth.profile",
                                username=session["user"]))

            else:
                # Invalid password, redirect to login page
                flash("Wrong Username and/ or Password")
                return redirect(url_for("auth.login"))
        else:
            # Username doesn't exist
            flash("Wrong Username and/ or Password")

    return render_template("login.html")


@auth.route("/profile")
def profile():
    # redirect to profile on login
    user = list(User.query.order_by(User.id).all())
    return render_template("profile.html")


@auth.route("/logout")
def logout():
    flash("You are logged out!")
    # logs user out
    session.pop("user")
    return redirect(url_for("home"))
