#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:16
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : __init__.py
# @Software: PyCharm

import sys
from pathlib import Path

from flask import Flask

from qff.app.api.v1.shop_endpoint_module_1 import bp as api_v1_bp
from qff.app.app_initiate import init_app_task
from qff.app.ext.ext import init_ext
from qff.app.views.views import bp as bp1
from qff.settings import settings
from qff.settings.settings import envs


def create_app():
    """
    创建flask app
    :return:
    """
    base_path = str(Path(__file__).resolve().parent)
    # print('============', base_path)
    if base_path not in sys.path:
        sys.path.append(base_path)

    app = Flask(__name__)  # type:Flask

    app.config.from_object(envs.get('D'))

    init_block(app=app)

    return app


def init_block(*, app):
    """
    flask初始化块
    :param app:
    :return:
    """
    init_ext(app=app)
    init_bp(app=app)
    init_app_task(app=app)
    # init_custom_task(app=app)


def init_bp(*, app):
    """
    初始化蓝图
    :param app:
    :return:
    """
    app.register_blueprint(blueprint=bp1)
    app.register_blueprint(blueprint=api_v1_bp)
