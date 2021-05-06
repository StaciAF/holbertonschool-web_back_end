#!/usr/bin/env python3
""" this module sets up REDIS """
from functools import wraps
from typing import Callable, Union
import redis
import uuid


def call_history(method: Callable) -> Callable:
    """ this method stores history for passed function """
    input_list_keys = method.__qualname__ + ":inputs"
    output_list_keys = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrap_call_history(self, *args) -> bytes:
        """ this function wraps count_history to persist details """
        self._redis.rpush(input_list_keys, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list_keys, output)
        return output
    return wrap_call_history


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

    @call_history
    @count_calls
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
