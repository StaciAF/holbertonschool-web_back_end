#!/usr/bin/env python3
""" this module creates a class BasicAuth """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ this class inherits from Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """ this method extracts base64 from BasicAuth """
        if authorization_header is None:
            return None
        if isinstance(authorization_header, str) is False:
            return None
        if authorization_header.startswith('Basic ') is False:
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ this method decodes base64 of auth_header
        Return - decoded authorization_header
        """
        if base64_authorization_header is None:
            return None
        if isinstance(base64_authorization_header, str) is False:
            return None
        try:
            return base64.b64decode(base64_authorization_header,
                                    None, False).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ this method extracts then returns credentials """
        colon = ':'
        if decoded_base64_authorization_header is None:
            return None, None
        if isinstance(decoded_base64_authorization_header, str) is False:
            return None, None
        if colon not in decoded_base64_authorization_header:
            return None, None
        else:
            credentials = decoded_base64_authorization_header.split(':')
            return credentials
