from flask import Flask, render_template, jsonify, request,session
from models import *
import os

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = r"postgres://axqhwdjtsatnmu:c065bdb14ba98663691563b16cae817e296f291494aaa56f926eadbb27a2ca22@ec2-34-200-72-77.compute-1.amazonaws.com:5432/d5i2dpm07892ig"
app.config["SQLALCHEMY_DATABASE_URI"] = r"postgresql://postgres:1@localhost:5432/project1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.secret_key = "abc"  
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
        return render_template("login.html")
    else:
        return render_template("error.html", message="The name has already existed.")
@app.route("/home", methods=["POST"])
def login():
    """Login."""
    # Get form information.
    name = request.form.get("name")
    password = request.form.get("password")

    session['username'] = name

    # Add user
    if User.query.filter_by(name=name,password=password).first() is None:
        return render_template("register.html")
    else:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'first.jpg')
        return render_template("home.html",user_image=full_filename,name=name )
@app.route("/register")
def turn_back_toregister():
    return render_template("register.html")

@app.route("/home")
def logout():
    session.pop('username', None)
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
    print(results[0].Author)
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'click.jpg')
    # print(full_filename)
    return render_template("resultSearching.html",results=results)

@app.route("/blog",methods=["POST"])
def blogRender():
    # title = request.form.get("title")
    # content = request.form.get("content")
    id = request.form.get("id")
    if id:
        blog = Blog.query.filter_by(id=id).all()
        print(type(blog[0]))
        author = blog[0].Author
        title = blog[0].title
        content = blog[0].content
        comments=Comment.query.filter_by(blog=title).all()
        message = True
        if len(comments) == 0:
            message = False
        return render_template("blog.html",title=title,content=content,author=author,comments=comments,message=message,alert=False)
    if id == None:
        user_name = session['username']
        content_comment = request.form.get("content")
        title = request.form.get("title")
        author = request.form.get("author")
        blog = Blog.query.filter_by(title=title).all()[0]
        contents = blog.content

        comments=Comment.query.filter_by(blog=title).all()
        message = True

        check_comment = Comment.query.filter_by(user=user_name).all()
        if len(check_comment)>0:
            return render_template("blog.html",title=title,content=contents,author=author,comments=comments,message=message,alert=True)
        else:
            new_comment = Comment(blog=title,content=content_comment,user=user_name)
            db.session.add(new_comment)
            db.session.commit()
            return render_template("blog.html",title=title,content=contents,author=author,comments=comments,message=message,alert=False)

if __name__ == "__main__":
    with app.app_context():
        main()