# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.status_code
~~~~~~~~~~~~~~~

"""
# error codes
PARAM_JSON_FORMAT_ERROR = 1001
PARAM_ERROR = 1002

NAME_OR_PASSWD_ERROR = 2001
USER_EMAIL_DUPLICATED = 2002
USER_NOT_FOUND = 2003

SERVER_INTERNAL_ERROR = 500

# hints
error_hints = {
    PARAM_JSON_FORMAT_ERROR: 'params should be json format',
    PARAM_ERROR: 'params are not valid, please check',

    NAME_OR_PASSWD_ERROR: 'user name or password error',
    USER_EMAIL_DUPLICATED: 'user email has been registered',
    USER_NOT_FOUND: 'user corresponding this email is not exist',

    SERVER_INTERNAL_ERROR: 'server internal error',
}
