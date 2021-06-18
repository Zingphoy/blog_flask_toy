# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.status_code
~~~~~~~~~~~~~~~

"""

NEED_JSON_FORMAT_PARAM = 1001
PARAM_ERROR = 10002

NAME_OR_PASSWD_ERROR = 2001

errors = {
    NEED_JSON_FORMAT_PARAM: 'params should be json format',
    PARAM_ERROR: 'params are not valid',

    NAME_OR_PASSWD_ERROR: 'user name or password error',
}
