# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.status_code
~~~~~~~~~~~~~~~

"""

NEED_JSON_FORMAT_PARAM = 1001

NAME_OR_PASSWD_ERROR = 2001

errors = {
    NEED_JSON_FORMAT_PARAM: 'params should be json format',

    NAME_OR_PASSWD_ERROR: 'user name or password error',
}
