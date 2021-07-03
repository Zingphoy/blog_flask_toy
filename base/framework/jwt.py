# -*- coding: utf-8 -*-

"""
blog_flask_toy/base/framework.jwt
~~~~~~~~~~~~~~~
jwt token implements here
"""
import os
import datetime as dt
import functools

from flask import abort
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt, get_jwt_identity, set_access_cookies
from flask_jwt_extended import create_access_token, create_refresh_token, current_user
from flask_jwt_extended.exceptions import NoAuthorizationError
from base.framework import get_flask_app, restful_response
from base import status_code
from user.user_model import User
from database import get_session
from utils import logger

app = get_flask_app()
EXPIRE_TIME = dt.timedelta(minutes=30)
REFRESH_TIME = dt.timedelta(days=3)

# 多数是flask_jwt_extended的默认设置，全部显式写出来提醒读者
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_IN_COOKIES'] = True
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_IDENTITY_CLAIM'] = 'signal'
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
app.config['JWT_JSON_KEY'] = 'access_token'
app.config['JWT_REFRESH_JSON_KEY'] = 'access_token'
app.config['JWT_REFRESH_COOKIE_NAME'] = 'refresh_token'
app.config['JWT_SECRET_KEY'] = 'my_app:' + str(os.urandom(16))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = EXPIRE_TIME  # 更容易过期的token，在重要接口验证时需要
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = REFRESH_TIME

__jwt = JWTManager(app)


# todo: 还可以基于jwt做用户访问屏蔽，但是需要数据库来保存（更简单是更新jwt写入一个block的标识，但是用户清除cookie后会丢失block信息）
# 官方方案参考 https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/

def admin_required(fn):
    """被装饰的路由只允许管理员访问"""

    @functools.wraps(fn)
    def decorator(*args, **kwargs):
        jwt_header, jwt_data = verify_jwt_in_request()
        claims = get_jwt()
        if claims.get('is_admin'):
            return fn(*args, **kwargs)
        else:
            return restful_response(status_code.OPERATION_NOT_PERMITTED)

    return decorator


def jwt_required(optional=False, fresh=False, refresh=False, locations=None):
    """flask_jwt_extended自带的jwt_required上添加异常捕捉"""

    def wrapper(fn):
        @functools.wraps(fn)
        def decorator(*args, **kwargs):
            try:
                verify_jwt_in_request(optional, fresh, refresh, locations)
            except Exception:
                abort(500, 'server internal error')
            return fn(*args, **kwargs)

        return decorator

    return wrapper


# @__jwt.user_identity_loader
# def user_identity_lookup(user):
#     """在jwt中添加一个sub字段，附上return的value"""
#     return user.id


@__jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    """"""
    logger.info(f'jwt header: {_jwt_header}, data: {jwt_data}')
    uid = jwt_data.get('signal')  # signal字段用作识别用户id，起了个奇怪的名字混淆视听
    if uid is None:
        return
    with get_session() as s:
        user = s.query(User.id).filter_by(id=uid).one_or_none()
    return user


@__jwt.additional_claims_loader
def add_claims_to_access_token(user):
    """生成新jwt时，添加user.id以识别不同用户"""
    return {
        'signal': user.id
    }


def is_token_expire():
    now = dt.datetime.now(dt.timezone.utc)
    exp_ts = get_jwt().get('exp')
    if exp_ts is not None and (now - EXPIRE_TIME) >= exp_ts:
        return True
    else:
        return False


@app.after_request
def refresh_expiring_token(response):
    try:
        verify_jwt_in_request()
    except NoAuthorizationError:
        # 不是所有请求都会带上正确jwt，对于没带jwt的请求，不做动作
        return response

    try:
        if is_token_expire():
            access_token = create_access_token(identity=get_jwt_identity(), fresh=True)
            refresh_token = create_refresh_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
            set_access_cookies(response, refresh_token)
    except (RuntimeError, KeyError) as e:
        logger.warning(f'error occurs: {e}')
    finally:
        return response


# todo: 还是单独放一个refresh接口用来更新access token吧

"""
预期流程：
1. login时生成token，token只在部分接口才需要被check
2. 在每次请求结束的时候check token是否过期，如果token没有携带，则不需要check
3. 如果token已经过期，重新生成token
"""

# # todo: 如果访问没带上jwt，是否可以把jwt的装饰器再封装，外部统一做try except返回response
# # login的时候赋予一个token
# @app.route('/token', methods=['POST'])
# @jwt_required(refresh=True)
# def refresh_token():
#     pass
