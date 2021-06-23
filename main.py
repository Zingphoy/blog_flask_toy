# -*- coding: utf-8 -*-

"""
blog_flask_toy.server.main
~~~~~~~~~~~~~~~

"""
import os

from flask import Flask, render_template, jsonify

from base.framework import ParamFormatInvalid

from flask_sqlalchemy_session import flask_scoped_session

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = os.urandom(16)

from database import session_factory
session = flask_scoped_session(session_factory, app)


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


def param_error(e):
    return jsonify()


@app.errorhandler(ParamFormatInvalid)
def email_too_long(e):
    return jsonify(e.to_dict())


"""
目标：只需直接raise异常，就能自动响应error code和提示

做法一：
在main.py中定义好所有专门的error处理函数，聚合成一个函数list，然后让所有的blueprint都register它们，也就是两个for循环

做法二：
每个异常类实现号对应的请求格式，逐个注册即可，直接注册到对应的blue_print下

"""


def run_server():
    from user.sign_on import sign_on
    app.register_blueprint(sign_on)

    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)

    app.run(port=8000, debug=True)


if __name__ == '__main__':
    run_server()
