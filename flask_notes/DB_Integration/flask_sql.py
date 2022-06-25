import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



# __file__ is this file's name
# find directory name
# Gather higher level folder names, i.e. users/kinkadedarling etc.
# This currently is: /Users/kinkadedarling/Desktop/Coding/python/Flask Udemy/Flask_Udemy_Notes/flask_notes/DB_Integration
# Is os agnostic and works on all  platforms.
# Allows for dynamic file routing.
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Creates migration capabilities
Migrate(app,db)
# export FLASK_APP=script_name.py
    # assigns the app directory for flask.
# flask db init
    # Sets up the migrations directory
# flask db migrate -m "message content"
    # set up the migration file
# flask db upgrade
    # updates the database with the migration


class Puppy(db.Model):
    # Manual override of table name
    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"{self.name} is {self.age} year/s old {self.breed}"
