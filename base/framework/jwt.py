# -*- coding: utf-8 -*-

"""
blog_flask_toy/base/framework.jwt
~~~~~~~~~~~~~~~
jwt token implements here
"""
import os
import datetime

from flask_jwt_extended import create_access_token, current_user, jwt_required, JWTManager
from base.framework.app import get_flask_app
from user.user_model import User
from database import get_session

app = get_flask_app()
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_SECRET_KEY'] = 'my_app:' + str(os.urandom(16))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

__jwt = JWTManager(app)


@__jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@__jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    print(jwt_data)
    with get_session():
        user = User.query.filter(User.id == jwt_data.get('sub')).first()
    return user
