#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:26
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : ext.py
# @Software: PyCharm

"""
第三方库模块
"""
from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from celery import Celery

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
toolbar = DebugToolbarExtension()
cache = Cache(with_jinja2_ext=False)
# celery_app = Celery('tasks', broker='redis://localhost:6379')


def init_ext(*, app):
    """
    初始化第三方库
    :return:
    """
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    bootstrap.init_app(app=app)
    toolbar.init_app(app=app)
    cache.init_app(app=app, config={'CACHE_TYPE': 'redis'})

