#!/usr/bin/env python3
""" Session authentication module. """

from api.v1.views import app_views
from flask import abort, jsonify, request
from api.v1.app import auth


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def session_logout() -> str:
    """ Implement logout. """
    try:
        auth.destroy_session(request)
    except Exception:
        abort(404)
    else:
        return jsonify({}), 200
