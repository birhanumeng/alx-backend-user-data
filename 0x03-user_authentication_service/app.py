#!/usr/bin/env python3
""" App module
"""

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index() -> str:
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
