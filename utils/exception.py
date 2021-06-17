#!/usr/bin/env python3
# ^_^ encoding: utf-8 ^_^

"""
utils.exception
~~~~~~~~~~~~~~


"""


class EmailTooLongException(BaseException):
    def __repr__(self):
        return 'length of user email too long'
