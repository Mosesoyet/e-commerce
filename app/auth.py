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

@auth.route('/login', strict_slashes=False)
def login():
    """The login page/form"""
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    """The login function for users"""
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash('User email or password is incorrect')
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.index'))

@auth.route('/signup', strict_slashes=False)
def signup():
    """The signup page for new users
    """
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    """The code for signup goes here
    """
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        """If user email is found then a new email should be
        used"""
        flash('User email exist')
        return redirect(url_for('auth.signup'))

    new_user = User(firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))
    

@auth.route('/logout', strict_slashes=False)
@login_required
def logout():
    """The code to logout a user"""
    logout_user()
    return redirect(url_for('main.index'))
