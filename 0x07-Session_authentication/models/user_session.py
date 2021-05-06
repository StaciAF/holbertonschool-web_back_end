#!/usr/bin/env python3
""" this module creates class UserSession """
from models.base import Base


class UserSession(Base):
    """ this method creates a new class inheritance from Base """
    def __init__(self, *args: list, **kwargs: dict):