from flask import (
    Flask,
    Blueprint,
    flash,
    render_template,
    request,
    redirect,
    url_for,
    session)
from wanderlist import app, db


error = Blueprint("error", __name__)


@error.app_errorhandler(400)
def handle_400(e):
    error_message = "Your request was interrupted. Please try again"
    return render_template('error.html', error_number="400",
                            error_message=error_message)


@error.app_errorhandler(401)
def handle_401(e):
    error_message = "You are not authorised to view this page. Please \
        check your details and try again."
    return render_template('error.html', error_number="401",
                            error_message=error_message)


@error.app_errorhandler(404)
def handle_404(e):
    error_message = "This page doesn't exist. Check what was typed in \
        the address bar."
    return render_template('error.html', error_number="404",
                            error_message=error_message)


@error.app_errorhandler(500)
def handle_500(e):
    error_message = "Something wrong with this webiste. Please try again."
    return render_template('error.html', error_number="500",
                            error_message=error_message)
