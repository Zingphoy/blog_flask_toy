# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.status_code
~~~~~~~~~~~~~~~

"""

NEED_JSON_FORMAT_PARAM = 1001
PARAM_ERROR = 1002

NAME_OR_PASSWD_ERROR = 2001
USER_EMAIL_DUPLICATED = 2002

SERVER_INTERNAL_ERROR = 500

errors = {
    NEED_JSON_FORMAT_PARAM: 'params should be json format',
    PARAM_ERROR: 'params are not valid',

    NAME_OR_PASSWD_ERROR: 'user name or password error',
    USER_EMAIL_DUPLICATED: 'user email has been registered',

    SERVER_INTERNAL_ERROR: 'server internal error',
}
