#!/usr/bin/python3
"""
A script that creates database connection and create the table
"""
import sqlite3


try:
    print("Establishing database connection")
    conn = sqlite3.connect('product.db')
    print("Connected to database")
    cur = conn.cursor()
    print("Creating the table for products")
    cur.execute("DROP TABLE IF EXISTS products")
    cur.execute("CREATE TABLE IF NOT EXISTS products\
        (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,\
        price TEXT NOT NULL, price_now TEXT NOT NULL, photo BLOB NOT NULL)")
    print("Table created")
    conn.commit()
    cur.close()
except sqlite3.Error as error:
    print("Can perform tasks", error)
finally:
    if conn:
        conn.close()
