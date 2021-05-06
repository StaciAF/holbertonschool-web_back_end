#!/usr/bin/env python3
"""
this module defines and type-annotates a sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ this function sums a list of ints and floats """
    return sum(mxd_list)
