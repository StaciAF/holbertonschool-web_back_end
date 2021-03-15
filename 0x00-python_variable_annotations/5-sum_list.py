#!/usr/bin/env python3
"""
this module defines a function sum_list with type annotation
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ this function sums a list of floats """
    return sum(input_list)
