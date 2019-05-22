#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : views.py
# @Software: PyCharm

from flask import Blueprint, Flask, request, render_template
import random

from sqlalchemy import and_, or_, not_

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
    user = User(f'Tom{random.randint(10, 100)}', '123123')

    db.session.add(user)
    db.session.commit()

    return 'add success'


@bp.route('/getusers/')
@bp.route('/userlist/')
def get_users():
    """
    获取用户列表
    :return:
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # 分页器
    pagination = db.session.query(User).paginate(page=page, per_page=per_page)
    # users = pagination.items  # 直接获取分页数据集

    # 手动分页
    # users = db.session.query(User).offset((page - 1) * per_page).limit(per_page)

    # User表所有数据
    # users = User.query.all()
    # users = db.session.query(User).all()

    # 读取id>=10的数据 __gt__ __lt__ __ge__ __le__
    # users = User.query.filter(User.id >= 10)

    # 筛选username='Tom2'的数据
    # users = User.query.filter_by(username='Tom2')

    # 读取username中包含"1"的数据
    # users = User.query.filter(User.username.contains('1'))

    # 读取username中以"Tom1"开始的数据
    # users = User.query.filter(User.username.startswith('Tom1'))

    # 按照username排序，跳过2条，长度为5
    # users = User.query.order_by("username").offset(2).limit(5)

    # 模糊查询 like
    # users = User.query.filter(User.username.like('%1%'))

    # and or in not
    # users = User.query.filter(User.id.in_([1, 3, 5, 7]))
    # users = User.query.filter(and_(User.id > 5, User.id < 20))
    # users = User.query.filter(or_(User.id <= 5, User.id >= 20))
    # users = User.query.filter(not_(User.id == 5))

    # for u in users:
    #     print(u.id)

    return render_template('user_list.html', pagination=pagination)


@bp.route('/getuser/')
def get_user():
    """
    获取用户
    :return:
    """
    # 获取id=10的数据
    # u = User.query.get(10)

    # 获取User表最后一条数据（先按照id倒序，再取第一条）
    u = db.session.query(User).order_by(User.id.desc()).first()

    return f'{u.id}\t{u.username}\t{u.password}'
