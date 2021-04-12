#!/usr/bin/env python3
"""
this module adds auth methods
"""


def _hash_password(password: str) -> str:
    """ this method hashes a pwd then returns hashed pwd """
    from bcrypt import gensalt, hashpw
    if password is None and isinstance(password, str) is False:
        return None
    else:
        password = password.encode('utf-8')
        hashed_pwd = hashpw(password, gensalt())
        return hashed_pwd
