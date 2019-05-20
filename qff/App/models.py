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

    def __init__(self, username, password):
        self.username = username
        self.password = password
