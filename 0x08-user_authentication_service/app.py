#!/usr/bin/python 3
"""
this module sets up Flask app, adds routes
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
    - jsonify message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
