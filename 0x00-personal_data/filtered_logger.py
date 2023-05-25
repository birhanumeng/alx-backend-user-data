#!/usr/bin/env python3
""" Seting up personal information data and logging. """

import re
from typing import List


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
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message

if __name__ == '__main__':
    main()
