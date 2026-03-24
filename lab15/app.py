"""
Nihar patel
march 24, 2026
lab 15: RESTful API and unit test in Flask app
"""
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory data (dictionary) 
items = {}

@app.route('/')
def index():
    return render_template('index.html')

#CREATE an item
@app.route('/items', methods =['POST'])
def create_item():
    # get-json method to read json data sent by teh client in an http request 
    data = request.get_json()

    #genrate a new unique id for the new item 
    item_id = str(len(items)+1)

    #add the data collect fo the new item
    items[item_id] = data

    #jsonify convets a python dictionary into a json response, and resurns status code as 201 (yor reques worked and new resource was cleared)
    return jsonify({'id':item_id,'item':data}), 201

# READ all items
@app.route('/items',methods = ['GET'])
def get_items():
    return jsonify(items)
# READ SINGLE ITEM
@app.route('/items/<item_id>',methods =['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if not item:
        #404 = server is rechaable but the item you asked for doesn't exiest
        return jsonify({'error':'Item not found'}), 404
    
    return jsonify(item)


if __name__ == '__main__':
    app.run(debug=True)