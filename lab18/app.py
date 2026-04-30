from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from config import Config

app = Flask(__name__)

#-------------------------
# LOADING PAGE
#-------------------------
@app.route('/')
def home():
    return redirect(url_for('login'))

#-------------------------
# LOGIN ROUTING
#-------------------------
@app.route('/login')
def login():

    return render_template("login.html")

#-------------------------
# SIGNUP ROUTING
#-------------------------
@app.route('/signup')
def signup():
    return render_template('signup.html')
#-------------------------
# RUN APP
#-------------------------
if __name__ == '__main__':
    app.run(debug=True)