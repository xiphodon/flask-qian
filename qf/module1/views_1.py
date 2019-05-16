#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:55
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : views_1.py
# @Software: PyCharm
from flask import Blueprint

bp = Blueprint('bp_1', __name__, url_prefix='/m1')


@bp.route('/index/')
def index():
    return f'hello {__name__}'
