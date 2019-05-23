#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : models.py
# @Software: PyCharm
from qff.App.ext import db


class User(db.Model):
    """
    用户模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    nikename = db.Column(db.String(20), unique=False, nullable=True)
    # 一对多关联，可关联出user所拥有的product列表
    # 级联查询属性，与表结构无关
    # 参数1：关联的model类名，参数2：反向引用参数（为Product模型加入user参数），参数3：懒加载
    products = db.relationship('Product', backref='user', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Product(db.Model):
    """
    产品模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    price = db.Column(db.String(20), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, price, user_id):
        self.name = name
        self.price = price
        self.user_id = user_id



