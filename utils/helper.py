# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.helper
~~~~~~~~~~~~~~~

"""

import re

from base.exception import EmailTooLongException


def is_valid_email(email):
    if len(email) >= 64:
        raise EmailTooLongException
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.DOTALL)
    if pattern.findall(email):
        return True
    else:
        return False
