#!/usr/bin/env python3
"""
this module augments a given function with type annotation
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """ this function returns key value from dict """
    if key in dct:
        return dct[key]
    else:
        return default
