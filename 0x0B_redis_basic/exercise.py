#!/usr/bin/env python3
""" this module sets up REDIS """
from functools import wraps
from typing import Callable, Union
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """ this decorator counts how many times a Cache method is called """
    @wraps(method)
    def wrap_count_calls(self, *args) -> bytes:
        """ this function wraps count_calls to persist method details """
        key = method.__qualname__
        self._redis.incr(key, 1)
        return method(self, *args)
    return wrap_count_calls


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

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """ this method gets value of passed key from Redis """
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ this method ensures key is of type str with typecast """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ this method ensure key is of type int with typecase """
        return self.get(key, int)
