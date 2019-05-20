#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 10:45
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : views_2.py
# @Software: PyCharm
from flask import Blueprint, url_for

bp = Blueprint('bp_2', __name__, url_prefix='/m2')


@bp.route('/index/')
def index():
    return f'hello {__name__}'


@bp.route('/bp_url/')
def bp_url():
    """
    跨蓝图调用
    :return:
    """
    return url_for('bp_1.index')
