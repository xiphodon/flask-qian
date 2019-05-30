#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:20
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : __init__.py
# @Software: PyCharm
from flask import Flask

from qff.App import settings
from qff.App.ext import init_ext
from qff.App.settings import envs
from qff.App.views import init_bp


def create_app():
    """
    创建flask app
    :return:
    """
    app = Flask(__name__, static_folder='../static', template_folder='../templates')  # type:Flask

    app.config.from_object(envs.get('D'))

    init_bp(app=app)
    init_ext(app=app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
