#!/usr/bin/env python3
"""
this module defines a type-annotated function that returns another function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ this function returns another function using previous function attr """
    def float_mult(a: float) -> float:
        return a * multiplier
    return float_mult
