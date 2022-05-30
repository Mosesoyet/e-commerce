#!/usr/bin/python3
"""
This file is used for authentication purposes
"""
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', strict_slashes=False) #The login route
def login():
    """The login page/form
    This page has the form for user login.
    return rendner_template('login.html')
    """
    return render_template('login.html')

@auth.route('/login', methods=['POST']) #The login function
def login_post():
    """Get user info and check if in database
    return redirect(url_for('main.login'))
    """
    email = request.form.get('email') #User email
    password = request.form.get('password') #User password
    remember = True if request.form.get('remember') else False #If user checked remember then it's True else user won't be remebered

    #Check user email in database and if not exists then the user is not registered
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('User email or password is incorrect')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))

@auth.route('/signup', strict_slashes=False) #The signup page
def signup():
    """The signup page for new users
    First check user email in database and if exists, user is redirected to login page
    else create new user
    """
    return render_template('signup.html')

@auth.route('/signup', methods=['POST']) #The signup function
def signup_post():
    """Get user info on form submit
    Then query database o check if user exists
    If not then create new user
    """
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() #Check user email in database
    if user:
        #If email is found then user is redirected to the login page
        flash('User email exist')
        return redirect(url_for('auth.signup'))

    #Create a new user if not exists
    new_user = User(firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user) #Add user to database
    db.session.commit() #Save the info

    return redirect(url_for('auth.login'))
    

@auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    """The code to logout a user"""
    logout_user()
    return redirect(url_for('main.index'))
