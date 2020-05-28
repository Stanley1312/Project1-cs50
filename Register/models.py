import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "Users"
    # __table_args__ = (db.UniqueConstraint('name'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    blogs = db.relationship("Blog", backref="Users", lazy=True)
    


    def add_blog(self, title, date):
        b = Blog(title=title, users=self.name,date=date)
        db.session.add(b)
        db.session.commit()
class Blog(db.Model):
    __tablename__ = "Blogs"
    # __table_args__ = (db.UniqueConstraint('users'),)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    ratings_count = db.Column(db.Integer, nullable=True)
    users_id = db.Column(db.Integer,db.ForeignKey("Users.id"),nullable=False)
    date = db.Column(db.String,nullable=False)
    # blog_id = db.Column(db.Integer, db.ForeignKey("Users.id"), nullable=False)
