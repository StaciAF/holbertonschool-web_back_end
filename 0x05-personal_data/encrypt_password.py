#!/usr/bin/env python3
"""
this module encrypts a password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypts a password and returns its hashed version """
    encodedPass = password.encode('utf-8')
    hashed = bcrypt.hashpw(encodedPass, bcrypt.gensalt())
    return hashed
