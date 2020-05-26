from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"postgres://upqibsjarcenfx:9a07cb6c83ac91c4249ba4df91cc1a15f7abde07afb7340c1f8d1d2124566bd3@ec2-50-17-90-177.compute-1.amazonaws.com:5432/dcd617up0jgviu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    """Register."""

    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")

    # try:
    #     flight_id = int(request.form.get("flight_id"))
    # except ValueError:
    #     return render_template("error.html", message="Invalid flight number.")

    # # Make sure the flight exists.
    # flight = Flight.query.get(flight_id)
    # if not flight:
    #     return render_template("error.html", message="No such flight with that id.")

    # Add user
    try:
        list_user = User.query.filter_by(name=name).first()
        return render_template("error.html", message="The name has already existed.")
    except ValueError:
        new_user = User(name=name,password=password)
        db.session.add(new_user)
    return render_template("success.html")