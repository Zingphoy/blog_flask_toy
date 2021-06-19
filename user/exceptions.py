# -*- coding: utf-8 -*-

"""
blog_flask_toy/user.exception
~~~~~~~~~~~~~~~

"""

from base import status_code as sc
from base.framework import CustomException

hints = sc.error_hints


class UserNotFound(CustomException):
    def __init__(self, code=sc.USER_NOT_FOUND, msg=hints.get(sc.USER_NOT_FOUND)):
        super().__init__(code, msg)


class EmailTooLong(CustomException):
    def __init__(self, code=sc.PARAM_ERROR, msg='email too long, max length is 64 characters'):
        super().__init__(code, msg)
