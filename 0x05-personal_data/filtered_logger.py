#!/usr/bin/env python3
"""
this module creates methods for a filtered logger
"""
import logging
import mysql.connector
import os
import re
from typing import List, Any
from datetime import datetime


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
    """ this method gets a logger """
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

def main():
    """ gets db connection, retrieves all rows in a table """
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM users")
    row = cur.fetchall()
    for row in rows:
        for col in row:
            print(col)
    

if __name__ == "__main__":
    main()