# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.helper
~~~~~~~~~~~~~~~

"""

import re

from base.exception import EmailTooLongException


def is_valid_email(email):
    if not email or isinstance(email, str) or len(email) >= 64:
        raise EmailTooLongException
    pattern = re.compile(r'[\w-.]+@[\w-]+(.[\w_-]+)+', re.DOTALL)
    if pattern.findall(email):
        return True
    else:
        return False
