#!/usr/bin/env python3
""" Seting up personal information data and logging. """

import re
from typing import List
import logging
import mysql.connector
from os import getenv


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """ It returns the log message obfuscated.
        Arguments:
            - fields: a list of strings representing all fields
            to obfuscate
            - redaction: a string representing by what the field
            will be obfuscated
            - a string representing the log line
            - a string representing by which character is separating
            all fields in the log line (message)
    """

    for f in fields:
        new_message = re.sub(f + "=.*?" + separator,
                f + "=" + redaction + separator, message)
    return new_message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializer """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ It filters values in incoming log records using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ This logger should be named "user_data" and only log up to
        logging.INFO level. It should not propagate messages to other
        loggers. It should have a StreamHandler with RedactingFormatter
        as formatter.
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' Description: you will connect to a secure holberton database to read a
                     users table. The database is protected by a username and
                     password that are set as environment variables on the
                     server named PERSONAL_DATA_DB_USERNAME (set the default as
                     "root"), PERSONAL_DATA_DB_PASSWORD (set the default as an
                     empty string) and PERSONAL_DATA_DB_HOST (set the default
                 as "localhost").

        The database name is stored in PERSONAL_DATA_DB_NAME.

        Implement a get_db function that returns a connector to the database
        (mysql.connector.connection.MySQLConnection object).

           - Use the os module to obtain credentials from the environment
           - Use the module mysql-connector-python to connect to the MySQL
             database (pip3 install mysql-connector-python)
    '''
    connection_db = mysql.connector.connection.MySQLConnection(
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'))

    return connection_db


def main():
    '''
        Description: Implement a main function that takes no arguments and
                     returns nothing.

        The function will obtain a database connection using get_db and
        retrieve all rows in the users table and display each row under a
        filtered format

        Filtered fields:
                          name
                          email
                          phone
                          ssn
                          password
    '''
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    log = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, fields))
        log.info(str_row.strip())

    cursor.close()
    database.close()


if __name__ == '__main__':
    main()
