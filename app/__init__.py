#!/usr/bin/python3
"""
The main app
"""
from flask import Flask #Flask for writing the app name
from flask_login import LoginManager #For managing users
from flask_sqlalchemy import SQLAlchemy #For setting up user database
import sqlite3 #For managing products database


db = SQLAlchemy() #db as SQLAlchemy database

def create_app():
    """The app creation and configuration
    Other files are imported and registered as blueprint here
    return app
    """
    app = Flask(__name__) #Assiged flask_app as app
    app.config['SECRET_KEY'] = 'trick' #The secret key for app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #The database for users

    db.init_app(app) #Add database to app

    login_manager = LoginManager() #LoginManager() to managed login users
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        """Load user if logged in
        """
        return User.query.get(user_id)


    from .auth import auth as auth_blueprint #Importing auth Blueprint
    app.register_blueprint(auth_blueprint) #Registering auth with app to get routes

    from .main import main as main_blueprint #Importing main Blueprint
    app.register_blueprint(main_blueprint) #Registering main with app

    return app
