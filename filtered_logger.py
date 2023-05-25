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
    for str in fields:
        new_message = re.sub(str + "=.*?" + separator,
                str + "=" + redaction + separator, message)
    return new_message
