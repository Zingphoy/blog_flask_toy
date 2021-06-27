# -*- coding: utf-8 -*-

"""
blog_flask_toy/utils.status_code
~~~~~~~~~~~~~~~

"""
# error codes
PARAM_JSON_FORMAT_ERROR = 1001
PARAM_ERROR = 1002
OPERATION_NOT_PERMITTED = 1003

NAME_OR_PASSWD_ERROR = 2001
USER_EMAIL_DUPLICATED = 2002
USER_NAME_DUPLICATED = 2003
USER_NOT_FOUND = 2004

SERVER_INTERNAL_ERROR = 500

# hints
error_hints = {
    PARAM_JSON_FORMAT_ERROR: 'params should be json format',
    PARAM_ERROR: 'params are not valid, please check',
    OPERATION_NOT_PERMITTED: 'operation is not permitted for normal user',

    NAME_OR_PASSWD_ERROR: 'user name or password error',
    USER_EMAIL_DUPLICATED: 'user email has been registered',
    USER_NAME_DUPLICATED: 'user name has been registered',
    USER_NOT_FOUND: 'user corresponding this email is not exist',

    SERVER_INTERNAL_ERROR: 'server internal error',
}
