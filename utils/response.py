# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.response
~~~~~~~~~~~~~~~

"""
from flask import jsonify

from utils import status_code


def restful_response(code: int = 0, msg: str = 'success', data: dict = dict()):
    if msg == 'success' and code in status_code.errors.keys():
        msg = status_code.errors[code]
    return jsonify({
        'code': code,
        'msg': msg,
        'data': data
    })
