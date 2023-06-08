#!/usr/bin/env python3
""" App module
"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world() -> str:
    """ Home page """
    payload = {"message": "Bienvenue"}
    return app.jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
