import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from wanderlist import routes  # noqa

from wanderlist.auth.routes import auth
app.register_blueprint(auth) # noqa