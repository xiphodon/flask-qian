#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:25
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : settings.py
# @Software: PyCharm

"""
配置资源
"""


def get_db_uri(db_info):
    """
    获取数据库uri
    :param db_info: 数据库信息
    :return:
    """
    engine = db_info.get('ENGINE')
    driver = db_info.get('DRIVER')
    user = db_info.get('USER')
    password = db_info.get('PASSWORD')
    host = db_info.get('HOST')
    port = db_info.get('PORT')
    db_name = db_info.get('DB_NAME')

    return f'{engine}+{driver}://{user}:{password}@{host}:{port}/{db_name}'


class BaseConfig:
    """
    配置基类
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = '123456789'
    DATABASE = dict()
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    """
    开发模式配置
    """
    DEBUG = True
    DATABASE = {
        "ENGINE": "mysql",
        # "DRIVER": "pymysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "DB_NAME": "flask_db"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(BaseConfig):
    """
    开发模式配置
    """
    TESTING = True
    DATABASE = {
        "ENGINE": "mysql",
        # "DRIVER": "pymysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "DB_NAME": "flask_db"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(BaseConfig):
    """
    开发模式配置
    """
    DATABASE = {
        "ENGINE": "mysql",
        # "DRIVER": "pymysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "DB_NAME": "flask_db"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'D': DevelopConfig,
    'T': TestingConfig,
    'P': ProductConfig
}




