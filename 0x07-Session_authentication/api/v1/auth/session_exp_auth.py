#!/usr/bin/env python 3
""" this module creates a SessionExpAuth class """
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """ this class inherits from SessionAuth """

    def __init__(self):
        """ this is the init method for SessionExpAuth """

    def create_session(self, user_id=None):
        """ this method creates a session returns its ID """

    def user_id_for_session_id(self, session_id=None):
        """ this method returns User id from dict """
