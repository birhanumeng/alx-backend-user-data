#!/usr/bin/env python3
""" Testing our app
"""

import requests


def register_user(email: str, password: str) -> None:
    """ Registering new user
    """
    res = requests.post('http://127.0.0.1:5000/users', data={
        'email': email,
        'password': password
    })
    assert res.status_code == 200
    assert res.json() == {'email': email, 'message': "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """ Check the login with wrong password
    """
    res = requests.post('http://127.0.0.1:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Check the login with the correct password
    """
    res = requests.post('http://127.0.0.1:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert res.status_code == 200
    assert res.json() == {'email': email, 'message': "logged in"}

    return res.cookies.get('session_id')


def profile_unlogged() -> None:
    """ Ccheck with empty session id
    """
    res = requests.get('http://127.0.0.1:5000/profile')
    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Check with the correct session id
    """
    res = requests.get('http://127.0.0.1:5000/profile', cookies={
        'session_id': session_id
    })
    assert res.status_code == 200
    assert res.json() == {'email': "guillaume@holberton.io"}


def log_out(session_id: str) -> None:
    """ Check the logout
    """
    res = requests.delete('http://127.0.0.1:5000/sessions', cookies={
        'session_id': session_id
    })
    assert res.status_code == 302


def reset_password_token(email: str) -> str:
    """ Check the reset password token
    """
    res = requests.post('http://127.0.0.1:5000/reset_password', data={
        'email': email,
    })
    assert res.status_code == 200
    return res.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Check update password
    """
    res = requests.put('http://127.0.0.1:5000/reset_password', data={
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    })
    assert res.status_code == 200
    assert res.json() == {'email': email, 'message': "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
