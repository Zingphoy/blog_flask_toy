# -*- coding: utf-8 -*-

"""
blog_flask_toy/base/framework.app
~~~~~~~~~~~~~~~

"""
import os

from flask import Flask

__instance = None


def init_app():
    app = Flask(__name__, template_folder='template')
    app.config['SECRET_KEY'] = os.urandom(16)

    return app


def get_flask_app():
    global __instance
    if __instance is None:
        __instance = init_app()
    return __instance
