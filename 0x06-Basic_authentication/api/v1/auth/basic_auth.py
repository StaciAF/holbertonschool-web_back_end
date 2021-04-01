#!/usr/bin/env python3
""" this module creates a class BasicAuth """
from api.v1.auth.auth import Auth
import base64
from models.user import User
from models.base import DATA
from typing import TypeVar


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

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ this method returns a User based on credentials """
        if user_email or user_pwd is None:
            return None
        if isinstance(user_email, str) is False:
            return None
        if isinstance(user_pwd, str) is False:
            return None
        if DATA.get('User') is None:
            return None
        emailSearch = User.search({'email': user_email})
        if emailSearch is None:
            return None
        for user in emailSearch:
            if user.email == user_email:
                return user
            if user.is_valid_password(user_pwd) is False:
                return None
            else:
                return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ this method overloads Auth and gets user instance """
        auth_head = super().authorization_header(request)
        if not auth_head:
            return None
        else:
            extract = self.extract_base64_authorization_header(auth_head)
            decode = self.decode_base64_authorization_header(extract)
            email, pwd = self.extract_user_credentials(decode)
            user = self.user_object_from_credentials(email, pwd)
            return user
