"""
Nihar Patel
lab 14, mini blog app using Flask
March 19, 2026
"""
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

# database connection
db = mysql.connector.connect(
    host = 'localhost',
    user = 'flaskuser',
    password = 'password123',
    database = 'blogDB'
)

# create a tool 'cursor' to be used to run queries in db
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_blog', methods=['POST'])
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']

    # check if user already exists
    cursor.execute("SELECT userid FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        # user already exists, use their id
        user_id = existing_user[0]
    else:
        # insert new user into table users
        cursor.execute("INSERT INTO users(username, email) VALUES (%s, %s)", (username, email))
        db.commit()
        user_id = cursor.lastrowid

    # insert data into table blog
    cursor.execute("INSERT INTO blog(user_id, title, content) VALUES (%s, %s, %s)", (user_id, title, content))
    db.commit()

    return redirect('/blogs')

@app.route('/blogs')
def blogs():
    cursor.execute("SELECT blog.id, users.username, blog.title, blog.content, blog.created_at FROM blog JOIN users ON blog.user_id = users.userid")

    # get all the data and store them in 'data'
    data = cursor.fetchall()

    return render_template('blogs.html', blogs=data)

if __name__ == '__main__':
    app.run(debug=True)