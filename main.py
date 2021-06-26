# -*- coding: utf-8 -*-

"""
blog_flask_toy.server.main
~~~~~~~~~~~~~~~

"""
import os

from flask import render_template, jsonify

from base.framework import ParamFormatInvalid, ParamError, get_flask_app


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


def init_server():
    app = get_flask_app()

    def common_error_handler(e):
        return jsonify(e.to_dict())

    # 实际上通过raise Exception的形式来返回异常，好像比较混乱，异常在内部处理，显示返回错误码，代码结构会更一致
    app.register_error_handler(ParamFormatInvalid, common_error_handler)
    app.register_error_handler(ParamError, common_error_handler)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)

    return app


def run_server():
    app = init_server()

    from user.sign_on import sign_on
    app.register_blueprint(sign_on)

    app.run(port=8000, debug=True)


if __name__ == '__main__':
    run_server()
