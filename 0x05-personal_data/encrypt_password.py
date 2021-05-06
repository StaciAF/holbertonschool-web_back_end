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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ this method checks if password is valid """
    encodedPass = password.encode('utf-8')
    if bcrypt.checkpw(encodedPass, hashed_password):
        return True
    else:
        return False
