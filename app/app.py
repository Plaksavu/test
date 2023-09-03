import os
import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    hostname = os.uname()[1]
    return jsonify({'hostname': hostname})

@app.route('/author', methods=['GET'])
def get_author():
    author = os.getenv("AUTHOR", "Unknown")
    return jsonify({'author': author})

@app.route('/id', methods=['GET'])
def get_id():
    unique_id = str(uuid.uuid4())
    return jsonify({'uuid': unique_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

