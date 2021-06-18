# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.login
~~~~~~~~~~~~~~~

"""

from flask import Blueprint, request

from base import restful_response
from utils import is_valid_email
from user.user_model import User
from database import Session

from base import status_code

sign_on = Blueprint('sign_on', __name__)


@sign_on.route('/login', methods=['POST'])
def user_login():
    req_data = request.get_json(force=True)
    if not req_data:
        return restful_response(status_code.NEED_JSON_FORMAT_PARAM)
    session = Session()
    user = session.query(User).filter(User.username == req_data.get('username')) \
        .filter(User.password == req_data.get('password')).first()
    session.commit()
    session.close()
    if user:
        return restful_response()
    else:
        code = status_code.NAME_OR_PASSWD_ERROR
        return restful_response(code)


@sign_on.route('/logout', methods=['POST'])
def user_logout():
    req_data = request.get_json(force=True)
    if not req_data:
        return restful_response(status_code.NEED_JSON_FORMAT_PARAM)
    return restful_response()


@sign_on.route('/register', methods=['POST'])
def user_register():
    req_data = request.get_json(force=True)
    if not req_data:
        return restful_response(status_code.NEED_JSON_FORMAT_PARAM)

    name, passwd, email = req_data.get('username'), req_data.get('password'), req_data.get('email')
    if not (name and passwd and email):
        return restful_response(status_code.PARAM_ERROR)

    if not is_valid_email(email):
        email = ''
    session = Session()
    is_exist = session.query(User).filter(User.email == email).first()
    if is_exist:
        # 看看flask怎么处理抛出的异常
        raise Exception('fuck you')
    session.add(User(username=name, password=passwd, email=email))
    session.commit()
    session.close()
    return restful_response()
