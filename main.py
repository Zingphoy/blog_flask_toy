# -*- coding: utf-8 -*-

"""
blog_flask_toy.server.main
~~~~~~~~~~~~~~~

"""
import os

from flask import Flask, render_template, jsonify

from base.framework import ParamFormatInvalid, PARAM_ERROR

app = Flask(__name__, template_folder='template')
app.config['SECRET_KEY'] = os.urandom(16)


def page_not_found(e):
    return render_template('404.html'), 404


def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(ParamFormatInvalid, PARAM_ERROR)
def param_error(e):
    return jsonify(e.to_dict())


def run_server():
    from user.sign_on import sign_on
    app.register_blueprint(sign_on)

    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)



    app.run(port=8000, debug=True)


if __name__ == '__main__':
    run_server()
