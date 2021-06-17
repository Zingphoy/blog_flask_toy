# -*- coding: utf-8 -*-

"""
blog_flask_toy.server.main
~~~~~~~~~~~~~~~

"""

from flask import Flask


def run_server():
    app = Flask(__name__)

    from user.sign_on import sign_on
    app.register_blueprint(sign_on)

    app.run(port=8000, debug=True)


if __name__ == '__main__':
    run_server()
