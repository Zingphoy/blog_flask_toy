# -*- coding: utf-8 -*-

"""
blog_flask_toy/server/user.login
~~~~~~~~~~~~~~~
基于jwt认证机制
"""
import re

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from base import status_code
from base.framework import restful_response, create_access_token, create_refresh_token, jwt_required, admin_required
from user.user_model import User
from user.exceptions import EmailTooLong
from database import get_session
from utils import logger

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


def transform_password(passwd):
    if passwd == '':
        return None
    return generate_password_hash(passwd, 'pbkdf2:sha256', 8)


""" ---------belows are routers--------- """


@sign_on.route('/register', methods=['POST'])
@jwt_required(optional=True)
def user_register():
    req_data = request.get_json(silent=True)
    if not req_data:
        return restful_response(status_code.PARAM_JSON_FORMAT_ERROR)
    name, passwd, email = req_data.get('username'), req_data.get('password'), req_data.get('email')

    if not (name and passwd and email) or not is_valid_email(email):
        return restful_response(status_code.PARAM_ERROR)

    with get_session() as s:
        is_email_exist = s.query(User.email).filter_by(email=email).one_or_none()
        if is_email_exist:
            return restful_response(status_code.USER_EMAIL_DUPLICATED)
        is_name_exist = s.query(User.username).filter_by(username=name).one_or_none()
        if is_name_exist:
            return restful_response(status_code.USER_NAME_DUPLICATED)
        s.add(User(username=name, password=transform_password(passwd), email=email))
        s.commit()
    return restful_response()


@sign_on.route('/login', methods=['POST'])
@jwt_required(optional=True)
def user_login():
    req_data = request.get_json(silent=True)
    if not req_data:
        return restful_response(status_code.PARAM_JSON_FORMAT_ERROR)

    with get_session() as s:
        user = s.query(User).filter_by(username=req_data.get('username')).one_or_none()
        if user and check_password_hash(user.password, req_data.get('password')):
            access_token = create_access_token(identity=user, fresh=True)
            refresh_token = create_refresh_token(identity=user)
            return restful_response(data={'access_token': access_token, 'refresh_token': refresh_token})
        else:
            return restful_response(status_code.NAME_OR_PASSWD_ERROR)


@sign_on.route('/logout', methods=['POST'])
@jwt_required(refresh=True)
def user_logout():
    req_data = request.get_json(silent=True)
    if not req_data:
        return restful_response(status_code.PARAM_JSON_FORMAT_ERROR)
    return restful_response()


@sign_on.route('/password_change', methods=['PUT'])
@jwt_required(fresh=True)
def user_password_change():
    pass


@sign_on.route('/', methods=['DELETE'])
@jwt_required()
def user_delete():
    """用户账号注销"""
    req_data = request.get_json(silent=True)
    if not req_data:
        return restful_response(status_code.PARAM_JSON_FORMAT_ERROR)

    name, passwd, email = req_data.get('username'), req_data.get('password'), req_data.get('email')
    if not (name and passwd and email):
        return restful_response(status_code.PARAM_ERROR)

    with get_session() as s:
        s.delete(User).filter_by(username=name, email=email, password=transform_password(passwd))
        s.commit()
    return restful_response()


# 测试jwt是否正常
@sign_on.route('/hi', methods=['GET'])
@jwt_required()
def say_hi():
    return restful_response()
