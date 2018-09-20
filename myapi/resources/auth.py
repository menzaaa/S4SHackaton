#!/usr/bin/env python

import functools
from flask import g, abort
from flask_httpauth import HTTPBasicAuth
from models import User

from db import session

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = session.query(User).filter_by(first_name = username_or_token).first()
        if not user or not user.verify_password(password):
            print("Nee man")
            return False
    g.user = user
    return True


@auth.login_required
def get(self):
    token = g.user.generate_auth_token()
    return jsonify({'token' : token.decode('ascii') })


# @auth.verify_password
# def verify_password(username, password):

#     print('login attempt')

#     """Validate user passwords and store user in the 'g' object"""
#     g.user = User.query.filter_by(username=username).first()
#     return g.user is not None and g.user.check_password(password)


def self_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('first_name', None):
            if g.user.first_name != kwargs['first_name']:
                abort(403)
        if kwargs.get('user_id', None):
            if g.user.id != kwargs['user_id']:
                abort(403)
        return func(*args, **kwargs)
    return wrapper
