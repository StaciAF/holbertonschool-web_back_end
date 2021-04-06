#!/usr/bin/env python3
"""
this module creates SessionAuth class
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ this class inherits from Auth for Session authenticaton """
