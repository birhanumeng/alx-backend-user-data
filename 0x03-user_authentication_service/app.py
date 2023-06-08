#!/usr/bin/env python3
""" App module
"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index() -> str:
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
