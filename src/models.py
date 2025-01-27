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

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)

class Species(db.Model):
    __tablename__ = 'species'
    uid = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    classification = db.Column(db.String(500), nullable=False)
    planet_uid = db.Column(db.Integer, ForeignKey('planets.uid'), nullable=False)

class Planets(db.Model):
    __tablename__ = 'planets'
    uid = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    gravity = db.Column(db.String(500), nullable=False)

    
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    planet_uid = db.Column(db.Integer, ForeignKey('planets.uid'), nullable=False)

class FavType(enum.Enum):
    Planets = "Planets"
    Species = "Species"
    People = "People"

class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, index=True)
    user_from_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True, nullable=False)
    external_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(500), nullable=False)
    type = db.Column(db.Enum (FavType), nullable=False, index=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e









