#!/usr/bin/env python3
"""
this module defines and type-annotates a to_kv function that returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ this function returns a tuple with str and float elements """
    return k, v ** 2
