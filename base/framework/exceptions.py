# -*- coding: utf-8 -*-

"""
blog_flask_toy/base/framework.exceptions
~~~~~~~~~~~~~~~

"""
from base.status_code import *


class CustomException(Exception):
    def __init__(self, code: int, msg: str, payload: dict = None):
        super().__init__()
        self.msg = msg
        self.status_code = code
        if payload and not isinstance(payload, dict):
            raise TypeError('payload should be dict type')
        self.payload = payload

    def to_dict(self):
        return {
            'code': self.status_code,
            'msg': self.msg,
            'data': self.payload
        }

    def __repr__(self):
        return f'Excepiotn {self.__name__}: ' \
               f'code={self.status_code}, msg={self.msg}, payload={self.payload}'


class ParamFormatInvalid(CustomException):
    def __init__(self, code=PARAM_JSON_FORMAT_ERROR,
                 msg=error_hints[PARAM_JSON_FORMAT_ERROR],
                 payload=None):
        super().__init__(code, msg, payload)


class ParamError(CustomException):
    def __init__(self, code=PARAM_ERROR,
                 msg=error_hints[PARAM_ERROR],
                 payload=None):
        super().__init__(code, msg, payload)
