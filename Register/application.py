from flask import Flask, render_template, jsonify, request
from models import *
import os

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = r"postgres://axqhwdjtsatnmu:c065bdb14ba98663691563b16cae817e296f291494aaa56f926eadbb27a2ca22@ec2-34-200-72-77.compute-1.amazonaws.com:5432/d5i2dpm07892ig"
app.config["SQLALCHEMY_DATABASE_URI"] = r"postgresql://postgres:1@localhost:5432/project1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
db.init_app(app)


def main():
    db.create_all()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def register():
    """Register."""
    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")

    # Add user
    if User.query.filter_by(name=name).first() is None:
        new_user = User(name=name,password=password)
        db.session.add(new_user)
        db.session.commit()
        return render_template("success.html")
    else:
        return render_template("error.html", message="The name has already existed.")
@app.route("/home", methods=["POST"])
def login():
    """Login."""
    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")

    # Add user
    if User.query.filter_by(name=name,password=password).first() is None:
        return render_template("register.html")
    else:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'first.jpg')
        return render_template("home.html",user_image=full_filename)

@app.route("/login")
def turn_back_toregister():
    return render_template("register.html")

@app.route("/home")
def logout():
    return render_template("login.html")

@app.route('/home2',methods=["POST"])
def searching():
    selection = request.form.get("selection")
    search = request.form.get("search")
    # print(selection)
    # print(search)
    message = True
    if selection == "Users":
        results = Blog.query.filter_by(Author=search).all()
    elif selection == "Rating":
        results = Blog.query.filter_by(ratings_count=search).all()
    elif selection == "Title":
        results = Blog.query.filter_by(title=search).all()
    elif selection == "Date":
        results = Blog.query.filter_by(date=search).all()

    if results == []:
        message = False

    # print(message)
    print(results[0].title)

    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'click.jpg')
    # print(full_filename)
    return render_template("resultSearching.html",results=results)

@app.route("/blog")
def blogRender():
    return render_template("blog.html")

if __name__ == "__main__":
    with app.app_context():
        main()