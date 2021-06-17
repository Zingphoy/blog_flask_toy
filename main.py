# -*- coding: utf-8 -*-

"""
blog_flask_toy.server.main
~~~~~~~~~~~~~~~

"""

from flask import Flask, render_template

app = Flask(__name__)


@app.handle_exception(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler
@app.handle_exception(500)
def internal_server_error(e):
    return render_template('500.html'), 500


def run_server():
    from user.sign_on import sign_on
    app.register_blueprint(sign_on)

    app.run(port=8000, debug=True)


if __name__ == '__main__':
    run_server()
