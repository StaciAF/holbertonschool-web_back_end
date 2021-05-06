# 0x05. Personal data

### Learning Objectives
* Examples of Personally Identifiable Information (PII)
* How to implement a log filter that will obfuscate PII fields
* How to encrypt a password and check the validity of an input password
* How to authenticate to a database using environment variables

### Tasks
#### 0. Regex-ing
Write a function called ``filter_datum`` that returns the log message obfuscated:
#### 1. Log formatter
Update the class to accept a list of strings ``fields`` constructor argument.
  * Implement the ``format`` method to filter values in incoming log records using ``filter_datum``. Values for fields in ``fields`` should be filtered
#### 2. Create logger
Implement a ``get_logger`` function that takes no arguments and returns a ``logging.Logger`` object
  * Create a tuple ``PII_FIELDS`` constant at the root of the module containing the fields from ``user_data.csv`` that are considered PII. ``PII_FIELDS`` can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you must hide in your logs. Use it to parameterize the formatter
#### 3. Connect to secure database
n this task, you will connect to a secure ``holberton`` database to read a ``users`` table. The database is protected by a username and password that are set as environment variables on the server named ``PERSONAL_DATA_DB_USERNAME`` (set the default as “root”), ``PERSONAL_DATA_DB_PASSWORD`` (set the default as an empty string) and ``PERSONAL_DATA_DB_HOST`` (set the default as “localhost”).
#### 4. Read and filter data
The function will obtain a database connection using ``get_db`` and retrieve all rows in the users table and display each row under a filtered format like this:
```
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
```
#### 5. Encrypting passwords
Implement a ``hash_password`` function that expects one string argument name ``password`` and returns a salted, hashed password, which is a byte string
#### 6. Check valid password
Implement an ``is_valid`` function that expects 2 arguments and returns a boolean