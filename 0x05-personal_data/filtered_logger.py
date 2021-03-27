#!/usr/bin/env python3
"""
this module creates methods for a filtered logger
"""
from typing import List
import re

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """ this method obfuscates data from log messages, returns new str with public details only """
    # fields is a list of keys
    # redaction is what keys:value should be replaced with
    # message is str to find fields and replace values
    # char given to separate each field
    # re.sub('value', redaction, str)
    for field in fields:
        regex = f"(?<={field}=).*?(?={separator})"
        message = re.sub(regex, redaction, message)
    return message
