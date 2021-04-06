#!/usr/bin/env python3
"""
this module creates a class Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """this creates the Auth class for API autorization """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """this method checks for excluded paths """
        slash = '/'

        if path is None or excluded_paths is None:
            return True
        if not excluded_paths:
            return True
        if path[-1] != slash:
            path += slash
        if path not in excluded_paths:
            return True
        else:
            return False

    def authorization_header(self, request=None) -> str:
        """this method returns None """
        authHeader = 'Authorization'

        if request is None:
            return None
        if request.headers.get(authHeader) is None:
            return None
        return request.headers.get(authHeader)

    def current_user(self, request=None) -> TypeVar('User'):
        """this method returns None"""
        return None
