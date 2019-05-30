#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 18:51
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : app_initiate.py
# @Software: PyCharm
from flask import Flask

from qff.app.ext import cache


def init_app_flow(*, app: Flask):
    """
    应用初始化流程
    :param app:
    :return:
    """
    clear_cache(app=app)


def clear_cache(*, app: Flask):
    """
    清除缓存
    :param app:
    :return:
    """
    with app.app_context():
        cache.clear()
