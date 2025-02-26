# Simple Flask Login Signup using SQLite
* [Based on Flask Login](https://github.com/eniompw/FlaskLogin)

## Overview
This is a simple web application built with Flask that demonstrates user authentication functionality (login and signup) using SQLite for data storage. The application allows users to create accounts and login with their credentials.

## Features
- User registration (signup)
- User authentication (login)
- SQLite database integration
- Simple web interface

## Code

### app.py
```python
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/select', methods=['post'])
def select():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?",
                    (request.form['un'],request.form['pw']))
    match = len(cur.fetchall())
    con.close()
    if match == 0:
        return "wrong username and password"
    else:
        return "welcome " + request.form['un']

@app.route('/insert', methods=['post'])
def insert():
	con = sqlite3.connect("login.db")
	cur = con.cursor()
	cur.execute(""" INSERT INTO users (username, password)
			VALUES (?, ?) """,
			(request.form['un'], request.form['pw']))
	con.commit()
	con.close()
	return 'signup successful'
```

## How to Run
1. Install the required dependencies from `requirements.txt`
2. Make sure the database is created using `create_table.py`
3. Run the Flask application using `python app.py`
4. Access the application in your web browser
