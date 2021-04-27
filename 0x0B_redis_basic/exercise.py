#!/usr/bin/env python3
""" this module sets up REDIS """
from typing import Union
import redis
import uuid


class Cache():
    """ creates new class Cache """
    def __init__(self):
        """ this method initializes the class Cache """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ this method creates rando key, stores input in Redis """
        key_gen = str(uuid.uuid4())
        self._redis.set(key_gen, data)
        return key_gen