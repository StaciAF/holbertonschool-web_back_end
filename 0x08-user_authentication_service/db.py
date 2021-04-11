#!/usr/bin/env python3
"""
this module creats a new class DB
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, InvalidRequestError
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

    def add_user(self, email: str, hashed_password: str):
        """ this method saves a user to db then returns a User object """
        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs):
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

    def update_user(self, user_id: int, **kwargs) -> None:
        """ this method finds_user_by and updates user attrs """
        user_attrs = ['id',
                      'email',
                      'hashed_password',
                      'session_id',
                      'reset_token']
        session = self._session
        this_user = self.find_user_by(id=user_id)
        for key, val in kwargs.items():
            if key not in user_attrs:
                raise ValueError
            this_user.key = val
            session.add(this_user)
            session.commit()
