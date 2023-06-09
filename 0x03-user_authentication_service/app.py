#!/usr/bin/env python3
""" App module
"""

from flask import Flask, jsonify, request, abort

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index() -> str:
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


@app.route('/users', methods=['POST'])
def register_users() -> str:
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    user = AUTH.register_user(email, password)
    if user:
        return jsonify({"email": email, "message": "user created"})
    else:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    form_data = request.form

    if "email" not in form_data:
        return jsonify({"message": "email required"}), 400
    if "password" not in form_data:
        return jsonify({"message": "password required"}), 400

    email = request.form['email']
    password = request.form['password']

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = {"email": email, "message": "logged in"}
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
