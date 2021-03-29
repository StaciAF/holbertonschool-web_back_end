#!/usr/bin/env python3
"""
this module creates methods for a filtered logger
"""
from typing import List, Any
import re
import logging
import mysql.connector
import os


PII_FIELDS = ('name','email', 'phone','ssn', 'password')

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ this method filters values of incoming log records """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)
                            
def get_logger(self) -> logging.Logger:
    userDataLGR = logging.getLogger('user_data')
    userDataLGR.setLevel(logging.INFO)
    userDataLGR.propagate = False
    console = logging.StreamHandler()
    console.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    userDataLGR.addHandler(console)
    return userDataLGR

def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ this method obfuscates data from log messages
    then returns new str with public details only """
    # fields is a list of keys
    # redaction is what keys:value should be replaced with
    # message is str to find fields and replace values
    # char given to separate each field
    # re.sub('value', redaction, str)
    for field in fields:
        regex = f"(?<={field}=).*?(?={separator})"
        message = re.sub(regex, redaction, message)
    return message

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ this method returns a MySQLConnection """
    host = os.environ['PERSONAL_DATA_DB_HOST']
    database = os.environ['PERSONAL_DATA_DB_NAME']
    user = os.environ['PERSONAL_DATA_DB_USERNAME']
    password = os.environ['PERSONAL_DATA_DB_PASSWORD']
    
    db = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    return db