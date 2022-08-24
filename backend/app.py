from crypt import methods
import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/get', methods = ['GET'])
def home():
    return jsonify({'uno': '1', 'dos': '2', 'tres':'3'})

if '__main__' == __name__:
    app.run(debug=True)