#!/usr/bin/env python3
""" App module
"""

from flask import Flask
from flask import jsonify
from flask import request

from auth import Auth

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    msg = {"message": "Bienvenue"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
