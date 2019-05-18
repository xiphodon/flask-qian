#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:55
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : models.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """
    初始化db
    :return:
    """
    db.init_app(app=app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
