# -*- coding: utf-8 -*-

"""
blog_flask_toy/base.error_handler
~~~~~~~~~~~~~~~

"""

from user.sign_on import sign_on
from base.exception import *


@sign_on.errorhandler(Exception)
def handler_exception(e):
    if isinstance(e, EmailTooLongException):
        pass

    if isinstance(e, Exception):
        pass
