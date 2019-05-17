#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 9:55
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : manager.py
# @Software: PyCharm
import redis as redis
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_session import Session
import os
import sys


base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# base_path = os.path.abspath(r'.')
if base_path not in sys.path:
    sys.path.append(base_path)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecretkey'

app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
# app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
# app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
# app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
# app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='123123')  # 用于连接redis的配置

Session(app=app)

manager = Manager(app=app)

bootstrap = Bootstrap(app=app)


def register_bp():
    """
    注册蓝图
    :return:
    """
    # print(sys.path)
    from qf.module1.views_1 import bp as bp_1
    app.register_blueprint(blueprint=bp_1)

    from qf.module1.views_2 import bp as bp_2
    app.register_blueprint(blueprint=bp_2)

    from qf.module1.user import bp as bp_3
    app.register_blueprint(blueprint=bp_3)


register_bp()

if __name__ == '__main__':
    manager.run()
