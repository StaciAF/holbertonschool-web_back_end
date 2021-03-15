#!/usr/bin/env python3
"""
this module updates given code with duck type annotation
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ this function has been augmented with duck-type annotation """
    if lst:
        return lst[0]
    else:
        return None
