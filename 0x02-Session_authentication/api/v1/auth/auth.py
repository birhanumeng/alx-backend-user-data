#!/usr/bin/env python3
""" Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Authentication class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Authentication method """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        # Add slash to all cases for consistency
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates user """
        return None
