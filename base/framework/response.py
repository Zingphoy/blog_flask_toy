# -*- coding: utf-8 -*-

"""
blog_flask_toy/base.framework
~~~~~~~~~~~~~~~
框架所需要的各种基本封装
"""
from flask import jsonify

from base import status_code


def restful_response(code: int = 0, msg: str = 'success', data=None):
    if msg == 'success' and code in status_code.error_hints.keys():
        msg = status_code.error_hints[code]
    return jsonify({
        'code': code,
        'msg': msg,
        'data': data
    })
