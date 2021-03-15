#!/usr/bin/env python3
"""
this module defines a function sum_list with type annotation
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
