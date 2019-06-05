#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : models.py
# @Software: PyCharm
from qff.app.ext.ext import db


class User(db.Model):
    """
    用户模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    nikename = db.Column(db.String(20), unique=False, nullable=True)
    create_datetime = db.Column(db.DateTime, unique=False, nullable=True)
    # 一对多关联，可关联出user所拥有的product列表
    # 级联查询属性，与表结构无关
    # 参数1：关联的model类名，参数2：反向引用参数（为Product模型加入user参数，懒加载），参数3：懒加载
    products = db.relationship('Product', backref=db.backref('user', lazy=True), lazy=True)

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


# 多对多中间表 FocusShop
focus_shop = db.Table(
    'focus_shop',
    db.Column('id', db.Integer, primary_key=True, autoincrement=True),
    db.Column('cstm_id', db.Integer, db.ForeignKey('customer.id')),
    db.Column('comp_shop_id', db.Integer, db.ForeignKey('company_shop.id'))
)


class CompanyShop(db.Model):
    """
    公司商店模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shop_name = db.Column(db.String(50), unique=False, nullable=False)
    company_name = db.Column(db.String(50), unique=False, nullable=True)

    # 多对多，级联查询
    # 商店关注者
    # 参数1：多对多的另一张表模型名，参数2：中间表模型，参数3：（懒加载）子查询，参数4：反向引用（给Customer模型加入focus_shops参数，懒加载）
    followers = db.relationship('Customer',
                                secondary=focus_shop, lazy='subquery',
                                backref=db.backref('focus_shops', lazy=True))

    def __init__(self, shop_name, company_name):
        self.shop_name = shop_name
        self.company_name = company_name


class Customer(db.Model):
    """
    消费者（顾客）模型
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wx_openid = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=False, nullable=True)

    def __init__(self, wx_openid, phone_number):
        self.wx_openid = wx_openid
        self.phone_number = phone_number

