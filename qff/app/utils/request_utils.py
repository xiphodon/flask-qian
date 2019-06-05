#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 17:49
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : request_utils.py
# @Software: PyCharm
from flask import request, jsonify


def is_method(method):
    """
    判断是否为请求指定方法
    :param method: 请求方法（GET/POST/PUT/DELETE...)
    :return:
    """
    return request.method == method


def switch_method(**kwargs):
    """
    选择指定请求方法
    :param kwargs: 请求参数键值对 eg: {'get': get_func, 'post': post_func}
    :return:
    """
    method = str(request.method).upper()
    method_func_dict = dict()

    for k, v in kwargs.items():
        method_func_dict[str(k).upper()] = v

    method_func = method_func_dict.get(method)
    if method_func and callable(method_func):
        return jsonify(method_func())

    return jsonify({})
