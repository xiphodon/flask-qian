#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:16
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask

from qff.app import settings
from qff.app.app_initiate import init_app_flow
from qff.app.ext import init_ext
from qff.app.settings import envs
from qff.app.views import init_bp

from pathlib import Path
import sys


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

    init_bp(app=app)
    init_ext(app=app)
    init_app_flow(app=app)

    return app



