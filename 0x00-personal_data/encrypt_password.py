#!/usr/bin/env python3
""" Encrypting passwords and chack validity of password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Takes one string as an argument name password and returns a salted,
        hashed password, which is a byte string using bcrypt package.
    """
    pwd_encoded = password.encode()
    pwd_hashed = bcrypt.hashpw(pwd_encoded, bcrypt.gensalt())

    return pwd_hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Takes two arguments and return 'True' if 'hashed_password' match
        with 'password' otherwise 'False'.
    """
    validity = False
    pwd_encoded = password.encode()
    if bcrypt.checkpw(pwd_encoded, hashed_password):
        validity = True
    return validity
