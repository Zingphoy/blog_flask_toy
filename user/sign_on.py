# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.login
~~~~~~~~~~~~~~~

"""

from flask import Blueprint, request
from werkzeug.security import generate_password_hash

from database import Session
from user.user_model import User
from utils import is_valid_email
from base import restful_response, status_code

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
        return restful_response(status_code.USER_EMAIL_DUPLICATED)
    salted_passwd = generate_password_hash(passwd, 'pbkdf2:sha256', 8)
    session.add(User(username=name, password=salted_passwd, email=email))
    try:
        session.commit()
    except Exception:
        session.close()
        return restful_response(status_code.SERVER_INTERNAL_ERROR)
    else:
        return restful_response()
    finally:
        session.close()


@sign_on.route('/', methods=['DELETE'])
def user_delete():
    req_data = request.get_json(force=True)
    if not req_data:
        return restful_response(status_code.NEED_JSON_FORMAT_PARAM)
    name, passwd, email = req_data.get('username'), req_data.get('password'), req_data.get('email')
    if not (name and passwd and email):
        return restful_response(status_code.PARAM_ERROR)

    salted_passwd = generate_password_hash(passwd, 'pbkdf2:sha256', 8)
    session = Session()
    session.query(User).filter(User.username == name, User.email == email, User.password == salted_passwd)
    try:
        session.commit()
    except Exception:
        session.close()
        return restful_response(status_code.SERVER_INTERNAL_ERROR)
    else:
        return restful_response()
    finally:
        session.close()
