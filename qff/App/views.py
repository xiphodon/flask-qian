#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, Flask

from qff.App.ext import db
from qff.App.models import User

bp = Blueprint('first_bp', __name__)


def init_bp(*, app: Flask):
    """
    初始化 blueprint
    :param app:
    :return:
    """
    app.register_blueprint(blueprint=bp)


@bp.route('/')
def index():
    return 'hello flask'


@bp.route('/adduser/')
def add_user():
    """
    添加用户
    :return:
    """
    user = User('Tom2', '123123')

    db.session.add(user)
    db.session.commit()

    return 'add success'


@bp.route('/getusers/')
def get_users():
    """
    获取用户列表
    :return:
    """
    users = User.query.all()
    users_str_list = list()

    for u in users:
        users_str_list.append(f'{u.username}\t{u.password}')

    return '<br/>'.join(users_str_list)
