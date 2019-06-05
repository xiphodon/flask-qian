#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 18:51
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : app_initiate.py
# @Software: PyCharm

from qff.app.ext.ext import cache
from flask import abort, render_template


def init_app_task(*, app):
    """
    初始化应用任务
    :param app:
    :return:
    """
    clear_cache(app=app)
    app_hook(app=app)


def clear_cache(*, app):
    """
    清除缓存
    :param app:
    :return:
    """
    with app.app_context():
        cache.clear()


def app_hook(*, app):
    """
    应用钩子
    :return:
    """

    @app.errorhandler(404)
    def catch_error_code(e):
        """
        捕获错误码404,重定向到指定页面
        :return:
        """
        print(e)
        return render_template('404.html')
