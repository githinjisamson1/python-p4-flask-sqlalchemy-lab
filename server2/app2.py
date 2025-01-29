#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(port=3000, debug=True)
