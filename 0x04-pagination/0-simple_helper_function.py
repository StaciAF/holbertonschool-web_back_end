#!/usr/bin/env python3
"""
this module creates a function index_range that takes two int args
"""


def index_range(page: int, page_size: int) -> tuple:
    """ returns start and end index as a tuple corresponding to params """
    rangeTup = ()
    if page == 1:
        rangeStart = 0
        rangeEnd = page * page_size
        rangeTup = (rangeStart, rangeEnd)
    else:
        rangeStart = (page - 1) * page_size
        rangeEnd = page * page_size
        rangeTup = (rangeStart, rangeEnd)
    return rangeTup
