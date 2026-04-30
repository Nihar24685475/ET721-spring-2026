import os
from flask import Flask, render_template, request, jsonify
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)

#--------------------------------------------------
#configuration
#--------------------------------------------------
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

ALLOWED_EXTENSION = {'png','jpg','jpeg','gif'}

#--------------------------------------------------
# MYSQL CONNECTION
#--------------------------------------------------
db_config = {
    'host':'localhost',
    'user':'flaskuser',
    'password': 'password123',
    'database':'image_app'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION

#--------------------------------------------------
# LOADING PAGE
#--------------------------------------------------
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM images ORDER BY uploaded_at DESC")
    images = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', images=images)

#--------------------------------------------------
# UPLOAD IMAGE
#--------------------------------------------------
@app.route('/upload', methods = ['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error':'No file part'}), 400
    
    file = request.files['image']

    if file.filename == '':
        return jsonify({'error':'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO images (filename) VALUES (%s)", (filename,))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Image uploaded successfully!'})
    
    return jsonify({'error':'Invalid file type'}), 400

#--------------------------------------------------
# delete an IMAGE
#--------------------------------------------------
@app.route('/delete/<int:image_id>' , methods=['DELETE'])
def delete_image(image_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary = True)

    #get filename
    cursor.execute("SELECT filename FROM images WHERE id = %s", (image_id,))
    image = cursor.fetchone()

    if not image :
        cursor.close()
        conn.close()
        return jsonify({'error':'Image not found'}),404
                       
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], image['filename'])
    
    # delete from database
    cursor.execute("DELETE FROM images WHERE id = %s", (image_id,))
    conn.commit()
    cursor.close()
    conn.close()

    # delete file form the folder
    if os.path.exists(filepath):
        os.remove(filepath)

    return jsonify({'message' : 'image deleted successfully'})
#--------------------------------------------------
# RUN APP
#--------------------------------------------------
if __name__ == '__main__':
    app.run(debug = True)
