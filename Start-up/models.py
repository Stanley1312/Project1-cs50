import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    blogs = db.relationship("Blog", backref="users", lazy=True)

    def add_blog(self, name):
        b = Blog(name=name, owner=self.name)
        db.session.add(b)
        db.session.commit()


class Blog(db.Model):
    __tablename__ = "Blogs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    comment = db.Column(db.String, nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    owner = db.Column(db.String,db.ForeignKey("Users.name"),nullable=False)
