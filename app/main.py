#!/usr/bin/python3
"""
The main app for connecting the home page of the website and other pages.
"""
from flask import Blueprint, render_template #Import Blueprint to connect later with app
from flask_login import login_required, current_user #These are used for authentication purposes
from . import db #The database used for storing user info
import sqlite3 #For connecting product database

def get_db_conn():
    """Connect to product database
    return connection
    """
    conn = sqlite3.connect('product.db') #Variable for connecting database
    conn.row_factory = sqlite3.Row #SQLITE stores data in row and this fetch each row
    return conn

main = Blueprint('main', __name__) #Passing main as name to Blueprint to be registered in app

@main.route('/', strict_slashes=False) #The landing page
def index():
    """The landing page for application
    return render_template('index.html')
    """
    return render_template('index.html')

@main.route('/product', strict_slashes=False) #The products page
def products():
    """
    The code for getting products and onload(),
    all products in database will be displayed.
    return render_template('products.html')
    """
    conn = get_db_conn() #Function for database connection using SQLITE3 assigned to varriable.
    cu = conn.cursor() #The connection cursor
    sql = """SELECT * FROM products""" #SQL query statement that selects all infos from the products table in products database
    products = cu.execute(sql).fetchall() #All products fetched will be stored in products which is used during display
    
    return render_template('products.html', products=products)

@main.route('/about', strict_slashes=False) #The about route(page)
def about():
    """This page contains all the informations about this website
    """
    return render_template('about.html')

@main.route('/faq', strict_slashes=False)
def faq():
    """This page contains the frequently asked questions about our service
    """
    return render_template('faq.html')

@main.route('/profile', strict_slashes=False) #The user profile page
@login_required 
#Only users with login access an access this page
def profile():
    """User info is displayed here
    """
    return render_template('profile.html', firstname=current_user.firstname, lastname=current_user.lastname, email=current_user.email)

@main.route('/cart', strict_slashes=False) #Logout page
@login_required
def Cart():
    """
    if user is authenticated:
    onclick of this function will logout the user
    """
    return render_template('cart.html')
