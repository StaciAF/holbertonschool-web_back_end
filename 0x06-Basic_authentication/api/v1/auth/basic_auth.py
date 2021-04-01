#!/usr/bin/env python3
""" this module creates a class BasicAuth """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ this class inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """ this method extract base64 from BasicAuth """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if authorization_header.startswith('Basic ') is False:
            return None
        else:
            return authorization_header[6:]
