#!/usr/bin/env python3
"""
this module creats a new class DB
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from sys import argv
from typing import List, TypeVar
from user import Base, User


class DB:
    """ this method names DB as a new class with no inheritance """
    def __init__(self):
        """ this method initiates DB class """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ this method saves a user to db then returns a User object """
        new_sess = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        new_sess.add(new_user)
        new_sess.commit()
        return new_user

    def find_user_by(self, **kwargs) -> List:
        """ this method takes in keyword args and returns match from list """
        session = self._session
        user_attrs = ['id',
                      'email',
                      'hashed_password',
                      'session_id',
                      'reset_token']
        for kwarg in kwargs:
            if kwarg not in user_attrs:
                raise InvalidRequestError
            else:
                user_found = session.query(User).filter_by(**kwargs).one()
                if not user_found:
                    raise NoResultFound
                else:
                    return user_found
