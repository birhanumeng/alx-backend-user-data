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

@app.route('/users', method=['POST'])
def users() -> str:
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    user = AUTH.register_user(email, password)
    if user:
        return jsonify({"email": email, "message": "user created"}), 400
    else:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
