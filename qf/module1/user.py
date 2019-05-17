#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 15:29
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : user.py
# @Software: PyCharm
from flask import Blueprint, render_template, request, redirect, url_for, make_response, session, flash

bp = Blueprint('user', __name__, url_prefix=None)


@bp.route('/home/')
def get_home_page():
    """
    获取主页
    :return:
    """
    # username = request.cookies.get('username')  # cookies 读取指定key
    username = session.get('username')  # session 读取指定key

    return render_template('home.html', username=username)


@bp.route('/login/')
def get_login_page():
    """
    获取登录页面
    :return:
    """
    return render_template('login.html')


@bp.route('/tologin/', methods=['GET', 'POST'])
def login():
    """
    登录
    :return:
    """
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'admin' and password == '123456':
        flash(f'登录成功{username}')

        resp = make_response(f'登录成功{username}')

        # resp.set_cookie('username', username)  # cookies设置指定key
        session['username'] = username  # session设置指定key

        return resp

    else:
        flash('用户名或密码错误')
        return redirect(url_for('user.get_login_page'))


@bp.route('/logout/')
def logout():
    """
    退出登录
    :return:
    """

    resp = redirect(url_for('user.get_home_page'))

    # resp.delete_cookie('username')  # cookies 删除指定key
    session.pop('username')  # session 删除指定key

    return resp
