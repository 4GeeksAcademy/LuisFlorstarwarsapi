import os
import sys
import enum
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Follower(db.Model):
    __tablename__ = 'follower'
    user_from_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True, nullable=False)
    user_to_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True, nullable=False)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    username = db.Column(db.String(250), nullable=False, index=True)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    comment_text = db.Column(db.String(500), nullable=True)
    author_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

class MediaType(enum.Enum):
    Photo = "Photo"
    Video = "Video"

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    type = db.Column(db.Enum (MediaType), nullable=False, index=True)
    url = db.Column(db.String(300), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e









