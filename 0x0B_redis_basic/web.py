#!/usr/bin/env python3
""" this module implements an expiring web cache and tracker """
from functools import wraps
from typing import Callable
import redis
import requests


init_redis = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """ this method counts function calls """
    @wraps(method)
    def wrap_count_call(*args) -> str:
        """ this method counts wrapped func calls """
        key = "count:{}".format(args[0])
        init_redis.incr(key, 1)
        init_redis.setex("count", 10, init_redis.get(key))
        return method(*args)
    return wrap_count_call


@count_calls
def get_page(url: str) -> str:
    """ this method gets content from HTML with URL then returns """
    resp = requests.get(url)
    return resp.text
