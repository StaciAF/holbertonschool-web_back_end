#!/usr/bin/env python3
"""
this module creats a new class DB
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


from user import Base, User


class DB:

    def __init__(self):
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
        session = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ this method takes in keyword args and returns match from list """
        session = self._session
        user_found = session.query(User).filter_by(**kwargs).one()
        return user_found

    def update_user(self, user_id: int, **kwargs) -> None:
        """ this method finds_user_by and updates user attrs """
        this_user = self.find_user_by(id=user_id)
        for key, val in kwargs.items():
            if hasattr(this_user, key):
                setattr(this_user, key, val)
                self._session.commit()
            else:
                raise ValueError
        return None
