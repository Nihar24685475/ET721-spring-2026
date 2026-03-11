"""
Nihar patel
Lab 11,introduction to flask
Mar 10 ,2026
"""

from flask import Flask , render_template
"""
create an object 'app' from flask module 
"""
app = Flask(__name__)

#set the routing to the main page 
#'route' decorator is used to access the root URL

@app.route('/')
def index():
    name = "Nihar patel"
    fruits = ['apple','orange','grape']
    fruit = 'orange'
    return render_template('index.html' , username = name, listfruits = fruits , f = fruit)

# endpoint refer t othe name of the view in an app
@app.route('/about')
def about():
    images = ['car.jpg','fox.jpg','sunset.jpg']
    return render_template('about.html',imagelist=images)

@app.route('/quotes')
def quotes():
    return '<h1>quotes</h1>'

#set the 'app' to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)

