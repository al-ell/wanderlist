from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user)
import os


# If app exists import data from env.py
if os.path.exists("env.py"):
    import env  # noqa


# Create app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == True:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQL_AlCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# Import db after loading frameworks to prevent load error
from wanderlist import routes  # noqa


# Blueprintsn used to create seperate authenication route for user db
from wanderlist.auth.routes import auth
app.register_blueprint(auth)  # noqa
