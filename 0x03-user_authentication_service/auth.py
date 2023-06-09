#!/usr/bin/env python3
""" Authentication Module
"""

from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ Returns a hashed password for input argument password.
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
        """ Generate uuid4 and return it as a string
        """
        return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Inialization
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registering a new user if it is not exit
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """ Check the pasword
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False
