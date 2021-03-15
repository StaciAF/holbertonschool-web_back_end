#!/usr/bin/env python3
"""
this module augments a given function with type annotation
"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar, None] = None
                     ) -> Union[Any, TypeVar]:
    """ this function returns key value from dict """
    if key in dct:
        return dct[key]
    else:
        return default
