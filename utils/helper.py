# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.helper
~~~~~~~~~~~~~~~

"""

import re


def is_valied_email(email):
    pattern = re.compile(r'[a-zA-Z]@.*?\.com', re.DOTALL)
    ret = pattern.findall(email)
    if ret:
        return True
    return False
