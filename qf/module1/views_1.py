#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:55
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : views_1.py
# @Software: PyCharm
from flask import Blueprint, render_template

bp = Blueprint('bp_1', __name__, url_prefix='/m1')


@bp.route('/index/')
def index():
    return f'hello {__name__}'


@bp.route('/index_b/')
def index_b():
    return render_template('index_b.html')


@bp.route('/index_b2/')
def index_b2():
    names = ['Lucy', 'Lili', 'Nick', 'Tom']
    numbers = range(1, 4)
    html_str = '<h1>html str</h1>'
    return render_template('index_b2.html', names=names, numbers=numbers, html_str=html_str)
