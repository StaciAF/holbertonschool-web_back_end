#!/usr/bin/env python3
"""
this module uses duck type to annotate an iterable object
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ this function is annotate with duck type """
    return [(i, len(i)) for i in lst]
