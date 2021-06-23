# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.login
~~~~~~~~~~~~~~~

"""
import re

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from database import session_factory
from user.user_model import User
from base import status_code
from base.framework import restful_response, ParamFormatInvalid
from user.exceptions import EmailTooLong
from utils import logger

from flask_sqlalchemy_session import current_session

sign_on = Blueprint('sign_on', __name__)

""" ---------exception handlers--------- """


@sign_on.errorhandler(EmailTooLong)
def email_too_long(e):
    return jsonify(e.to_dict())


""" ---------utility methods--------- """


def is_valid_email(email):
    if len(email) >= 64:
        raise EmailTooLong()
    pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", re.DOTALL)
    if pattern.findall(email):
        return True
    else:
        return False


# @sign_on.before_request
# def init_database_session():
#     session['db_session'] = pickle.dumps(session_factory(), protocol=5)
#     print('init')
#
#
# @sign_on.teardown_request
# def close_database_session():
#     if 'db_session' not in session:
#         return
#     s = pickle.loads(session['db_session'])
#     try:
#         session_close = getattr(s, 'close')
#         session_close()
#     except AttributeError:
#         pass
#     print('close')


""" ---------belows are routers--------- """


@sign_on.route('/login', methods=['POST'])
def user_login():
    req_data = request.get_json(silent=True)
    if not req_data:
        raise ParamFormatInvalid()
    logger.info(f'{id(current_session)}')
    user = current_session.query(User).filter(User.username == req_data.get('username')) \
        .filter(User.password == req_data.get('password')).first()
    if user:
        return restful_response()
    else:
        code = status_code.NAME_OR_PASSWD_ERROR
        return restful_response(code)


@sign_on.route('/logout', methods=['POST'])
def user_logout():
    req_data = request.get_json(silent=True)
    if not req_data:
        raise ParamFormatInvalid()
    return restful_response()


@sign_on.route('/register', methods=['POST'])
def user_register():
    req_data = request.get_json(silent=True)
    if not req_data:
        raise ParamFormatInvalid()
    name, passwd, email = req_data.get('username'), req_data.get('password'), req_data.get('email')
    if not (name and passwd and email):
        return restful_response(status_code.PARAM_ERROR)

    if not is_valid_email(email):
        email = ''
    is_exist = current_session.query(User).filter(User.email == email).first()
    logger.info(is_exist)
    if is_exist:
        logger.info('???')
        return restful_response(status_code.USER_EMAIL_DUPLICATED)
    salted_passwd = generate_password_hash(passwd, 'pbkdf2:sha256', 8)
    current_session.add(User(username=name, password=salted_passwd, email=email))
    current_session.commit()

    logger.info(f'{id(current_session)}')
    return restful_response()

    # todo: 还是直接去理解sqlalchemy的session吧，理解完后再回来自己封装，目标时减少五位的commit rollback


@sign_on.route('/', methods=['DELETE'])
def user_delete():
    req_data = request.get_json(silent=True)
    if not req_data:
        raise ParamFormatInvalid()
    name, passwd, email = req_data.get('username'), req_data.get('password'), req_data.get('email')
    if not (name and passwd and email):
        return restful_response(status_code.PARAM_ERROR)

    salted_passwd = generate_password_hash(passwd, 'pbkdf2:sha256', 8)
    current_session.query(User).filter(User.username == name, User.email == email, User.password == salted_passwd)
