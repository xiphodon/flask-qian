#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:22
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : manager.py
# @Software: PyCharm
from flask import Flask, render_template, url_for
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app=app)


@app.route('/hello/<string:name>/', methods=['GET'])
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/any/<any(i, you, he, "123"):name>/', methods=['GET', 'POST'])
def hello_any(name):
    return render_template('hello.html', name=name)


@app.route('/url/')
def get_url():
    """
    反向解析
    :return:
    """
    url = url_for('hello_any', name='you')  # /any/you/
    return url


@app.route('/getphone/')
def get_phone():
    return '139-0000-1111'


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    manager.run()  # python manager.py runserver -d -r -h 0.0.0.0 -p 5000
