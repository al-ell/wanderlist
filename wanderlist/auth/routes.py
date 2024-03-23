import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for
from wanderlist import app, db
from wanderlist.models import Itineraries, Journal
from wanderlist.countries_api import get_countries
import json

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/register")
def register():
    return render_template("register.html")
