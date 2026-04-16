from flask import Flask, render_template, request, jsonify  
import mysql.connector 

app = Flask(__name__)

# ----------------
# database config
# ----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'password123'  
app.config['MYSQL_DB'] = 'todo_db'

db = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],       
    user=app.config['MYSQL_USER'],      
    password=app.config['MYSQL_PASSWORD'],  
    database=app.config['MYSQL_DB']
)

# --------------
# home route
# --------------
@app.route('/')
def index():
    return render_template('index.html') 

# --------------
# get all task
# --------------
@app.route('/get_tasks', methods = ['GET'])
def get_tasks():
    try:
        with db.cursor(dictionary = True) as cursor:
            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()
        return jsonify(tasks)
    except mysql.connector.Error as e:
        return jsonify({"error : str(e)"}),500
    
# --------------
#  app new task
# --------------
@app.route('/add_task', methods = ['POST'])
def add_task():
    data = request.get_json()
    task = data.get('task')

    if task:
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()
        cursor.close()
        return jsonify({'status' : 'success'})
    return jsonify ({'status': 'error'})

# --------------
# delete a task
# --------------
@app.route('/delete_task', methods =['POST'])
def delete_task():
    data = request.get_json()
    task_id = data.get('id')
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))

    db.commit()
    cursor.close()
     
    return jsonify({'status' : 'deleted'})

# --------------
# run app
# --------------

if __name__ == '__main__':
    app.run(debug=True)
