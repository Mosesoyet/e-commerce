#!/usr/bin/python3
"""
This is the base model
"""
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    """A class for the user model
    """
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(1000))
