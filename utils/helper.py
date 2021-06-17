# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.helper
~~~~~~~~~~~~~~~

"""

import re

from utils.exception import EmailTooLongException


def is_valid_email(email):
    if len(email) >= 64:
        raise EmailTooLongException
    pattern = re.compile(r'[\w-.]+@[\w-]+(.[\w_-]+)+', re.DOTALL)
    ret = pattern.findall(email)
    if ret:
        return True
    return False
