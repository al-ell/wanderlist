import os
from flask import Flask
from wanderlist import app, db


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        # Switch from DEBUG before deployment
        debug=os.environ.get("DEBUG")
    )
