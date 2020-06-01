from flask import Flask, render_template, jsonify, request,session,redirect,url_for
from models import *
import os

PEOPLE_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = r"postgres://qgorardefomjqz:ebcb07859a907fe7ab36b6738c6e8f4d475e6a5457a4d9c8be656c9350b45e29@ec2-54-161-208-31.compute-1.amazonaws.com:5432/d2metr5n3omthh"
# app.config["SQLALCHEMY_DATABASE_URI"] = r"postgresql://postgres:1@localhost:5432/project1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.secret_key = "abc"  
db.init_app(app)
list_drone = [] 

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
    # if 'username' in session:
    #     user = session['username']
    #     print(user)
    # print("adfadfkasndfoasdnfasdf")
    # # Add user
    if User.query.filter_by(name=name,password=password).first() is None:
        return render_template("register.html")
    else:
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'first.jpg')
        return render_template("home.html",user_image=full_filename,name=name)
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
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'first.jpg')
        return render_template("home.html",user_image=full_filename,message=message)
    # print(results[0].Author)
    # full_filename = os.path.join(app.config['UPLOAD_FOLDER'],'click.jpg')
    # print(full_filename)
    return render_template("resultSearching.html",results=results)

@app.route("/blog/",methods=["POST","GET"])
def blogRender():
    user_name = session['username']
    
    # content = request.form.get("content")
    # title = request.form.get("title")
    # if content and title is not None:
    id = request.form.get("id")
    # print("dsjdasdsafsdkb")
    # print("id:")
    # print(id)
    if id:
        blog = Blog.query.filter_by(id=id).all()
        print(type(blog[0]))
        author = blog[0].Author
        title = blog[0].title
        content = blog[0].content
        comments=Comment.query.filter_by(blog=title).all()
        
        message = True
        print("ajsdfasdfjasd")
        print(author)
        print(title)
        print(comments)
        print(content)
        if len(comments) == 0:
            message = False
        # return redirect(url_for('blog_id',id=id,title=title))
        return render_template("blog.html",title=title,content=content,author=author,comments=comments,message=message,username=user_name)

    if id == None:
        user_name = session['username']
        print("bla badsaihddsifbdugfuefnbeuifdsjfniu4564165198654")
        print(user_name)
        content_comment = request.form.get("content_comment")
        drone = request.form.get("drone")
        drone = int(drone)
        
        list_drone.append(drone)
        drone = sum(list_drone)/ len(list_drone)
        title = request.form.get("title")
        # if drone and title is not None:
        #     count += 1 
        print(title)
        author = request.form.get("author")
        blog = Blog.query.filter_by(title=title).all()[0]
        contents = blog.content
        new_comment = Comment(blog=title,content=content_comment,user=user_name)
        print(new_comment.date)
        db.session.add(new_comment)
        db.session.commit()
        print("asdfasdfasdasdfdasf")
        comments=Comment.query.filter_by(blog=title).all()
        count = len(comments)
        message = True
        # return redirect(url_for('blog_id',id=id))
        return render_template("blog.html",title=title,content=contents,author=author,comments=comments,message=message,username=user_name,count=count,drone=drone)

# @app.route("/blog/<id>")
# def blog_id(id):
#     user_name = session['username']
#     blog = Blog.query.filter_by(id=id).all()[0]
#     # print(type(blog[0]))
#     author = blog.Author
#     title = blog.title
#     content = blog.content
#     comments=Comment.query.filter_by(blog=title).all()
#     message = True
#     if len(comments) == 0:
#         message = False
#     count = len(comments)
#     return render_template("blog.html",title=title,content=content,author=author,comments=comments,message=message,username=user_name,count=count)



if __name__ == "__main__":
    with app.app_context():
        main()