#!/usr/bin/env python3
"""
this module creates a new Flask view for Session authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_sess_login():
    """ POST /api/v1/auth_session/login
    Return:
      - dict repr of User
    """
    u_email = request.form.get('email')
    u_pwd = request.form.get('password')

    if u_email is None or u_email == "":
        return jsonify({"error": "email missing"}), 400
    elif u_pwd is None or u_pwd == "":
        return jsonify({'error': 'password missing'}), 400
    emailSearch = User.search({'email', u_email})
    if emailSearch == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in emailSearch:
        if not user.is_valid_password(u_pwd):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            get_sess_name = os.getenv('SESSION_NAME')
            make_sess_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(get_sess_name, make_sess_id)
            return response
