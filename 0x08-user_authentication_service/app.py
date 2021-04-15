#!/usr/bin/env python3
"""
this module sets up Flask app, adds routes
"""
from auth import Auth
from flask import Flask, abort, jsonify, request

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
    - jsonify payload {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /
    Return:
    - jsonify user created or already registered
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if AUTH.register_user(email, password):
            return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ this method creates a new session for the user,
    stores it, returns JSON payload """
    email = request.form.get('email')
    password = request.form.get('password')
    validated = AUTH.valid_login(email, password)
    if validated:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
