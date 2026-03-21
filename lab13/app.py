"""
Nihar patel
March 17,2026
lab 13: simple submission form to simulate a full-stack app
"""
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysql config
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'
app.config['MYSQL_DB'] = 'employee_data'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    msg =" "

    if request.method =='POST':
        name = request.form['name']
        age = request.form['age']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee (name,age) VALUES (%s, %s)" , (name,age))
        mysql.connection.commit()
        cur.close()
        
        msg = "Data inserted successfully"

    return render_template('index.html', msg = msg)

if __name__ == '__main__':
    app.run(debug = True)