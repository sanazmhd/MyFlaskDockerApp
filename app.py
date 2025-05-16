from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='frontend/build')
CORS(app)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello Sanaz from Flask!'})

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
