#!/usr/bin/env python3
"""
this module corrects a given program to comply with mypy style
"""
from typing import Tuple, List, Any, cast


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ this function has been corrected with type annotation """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
