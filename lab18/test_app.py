"""
Nihar Patel
May 5, 2026
lab19 : unit test for veryfing auuthentication in Flask-SQLite app
"""
import os
import sqlite3
import pytest
from app import app 
# ---------------------- 
# TEST DATABASE SETUP 
#-----------------------
TEST_DB = "test_flask_auth.db"

def init_test_db():
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

@pytest.fixture
def client(monkeypatch):
    def test_get_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn
    
    monkeypatch.setattr("app.get_db", test_get_db)

    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'

    init_test_db()

    with app.test_client() as client:
        yield client

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
# ---------------------- 
# TEST HOME REDIRECT 
# ----------------------
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert '/login' in response.location

#------------------------
#TEST LOGIN SUCCESS
#------------------------
def test_login_success(client):
    #fisrt create a user to test the login later
    client.post('/signup', data={
    "username": "loginuser",
    "email": "login@example.com",
    "password": "123456"
})

    #test the login with the user infor above
    response = client.post('/login', data = {
        "email" : "login@example.com",
        "password" : "123456"
    }, follow_redirects = True)

    #assert testing
    assert response.status_code == 200
    #convert the <h1> welcome </h1> in dashboared.html into bytest object
    assert b"Welcome" in response.data

# --------------------
# TEST LOGIN FAILURE
#---------------------
def test_login_failure(client):
    response = client.post('/login', data = {
        "email" : "login@example.com",
        "password" : "wrong123"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data

#-------------------
#TEST SIGNUP
#-------------------
def test_signup(client):
    response = client.post('/signup', data = {
        "username" : "testuser",
        "email" : "test@example.com",
        "password" : "123456"
    }, follow_redirects = True)

    assert response.status_code == 200
    assert b"Account created successfully!" in response.data