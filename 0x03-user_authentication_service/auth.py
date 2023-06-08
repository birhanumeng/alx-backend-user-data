#!/usr/bin/env python3
""" Authentication Module
"""

from bcrypt import hashpw, gensalt, checkpw


def _hash_password(password: str) -> str:
    """ Returns a hashed password for input argument password.
    """
    return hashpw(password.encode('utf-8'), gensalt())
