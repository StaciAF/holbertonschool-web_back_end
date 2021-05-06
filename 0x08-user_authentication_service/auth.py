#!/usr/bin/env python3
"""
this module adds auth methods
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ this method hashes a pwd and saves user to db """
        if not isinstance(email, str) or not isinstance(password, str):
            return None
        try:
            self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            return self._db.add_user(email, hashed_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """ this method validates a user via email and pwd """
        if isinstance(email, str) is True and\
                isinstance(password, str) is True:
            try:
                hello_user = self._db.find_user_by(email=email)
                if hello_user:
                    if bcrypt.checkpw(password.encode(),
                                      hello_user.hashed_password):
                        return True
                    else:
                        return False
            except NoResultFound:
                return False

    def create_session(self, email: str) -> str:
        """ this method finds user,
        creates uuid, store in db,
        return session_id """
        if isinstance(email, str):
            try:
                sess_user = self._db.find_user_by(email=email)
                if sess_user:
                    session_id = _generate_uuid()
                    self._db.update_user(sess_user.id, session_id=session_id)
                    return session_id
            except NoResultFound:
                return None

    def get_user_from_session_id(self, session_id: str) -> User or None:
        if not session_id or session_id is None:
            return None
        else:
            try:
                return self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                return None

    def destroy_session(self, user_id: int) -> None:
        """ this method updates then returns session_id to None """
        if user_id is None or isinstance(user_id, int) is False:
            return None
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            return None


def _hash_password(password: str) -> str:
    """ this method hashes a pwd then returns hashed pwd """
    from bcrypt import gensalt, hashpw
    if password is None and isinstance(password, str) is False:
        return None
    else:
        password = password.encode('utf-8')
        hashed_pwd = hashpw(password, gensalt())
        return hashed_pwd


def _generate_uuid() -> str:
    """ this method creates then returns unique id """
    return str(uuid.uuid4())
