#!/usr/bin/python3
"""
The main app for connecting the home page of the website and other pages
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
import sqlite3

def get_db_conn():
    conn = sqlite3.connect('product.db')
    conn.row_factory = sqlite3.Row
    return conn

main = Blueprint('main', __name__)

def writeBinary(filename):
    with open(filename, 'wb') as fh:
        pic = fh.write()
        return pic
@main.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@main.route('/product', strict_slashes=False)
def products():
    """
    The code for getting products
    """
    conn = get_db_conn()
    cu = conn.cursor()
    sql = """SELECT * FROM products"""
    products = cu.execute(sql).fetchall()
    #writeBinary(products[4])
    return render_template('products.html', products=products)

@main.route('/about', strict_slashes=False)
def about():
    """This page contains all the informations about this website
    """
    return render_template('about.html')

@main.route('/faq', strict_slashes=False)
def faq():
    return render_template('faq.html')

@main.route('/profile', strict_slashes=False)
@login_required
def profile():
    return render_template('profile.html', firstname=current_user.firstname, lastname=current_user.lastname, email=current_user.email)

@main.route('/cart', strict_slashes=False)
@login_required
def Cart():
    return render_template('cart.html')
