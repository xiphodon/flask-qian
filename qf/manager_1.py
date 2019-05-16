#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:22
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : manager_1.py
# @Software: PyCharm

from flask import Flask, render_template, url_for, request, make_response, Response, redirect, abort, jsonify
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app=app)


@app.route('/index/')
def index():
    """
    无参路由
    :return:
    """
    return 'hello index'


@app.route('/hello/<string:name>/', methods=['GET'])
def hello(name):
    """
    带参路由
    converter: int/string/path/uuid/float/any ...  不写类型默认为string:
    :param name:
    :return:
    """
    return render_template('hello.html', name=name)


@app.route('/any/<any(i, you, he, "123"):name>/', methods=['GET', 'POST'])
def hello_any(name):
    """
    带参路由 any
    仅允许/any/i/ /any/you/ /any/he/ /any/123/ url
    :param name:
    :return:
    """
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
    """
    无参路由
    获取手机号码
    :return:
    """
    return '139-0000-1111'


@app.route('/req_resp/')
def req_resp():
    """
    request & response
    :return:
    """
    #  http://127.0.0.1:9000/req_resp/?user=nihao&age=10
    print('request.path= ', request.path)
    print('request.headers= ', request.headers)
    print('request.json= ', request.json)
    print('request.data= ', request.data)
    print('request.args= ', request.args)
    print('request.method= ', request.method)
    print('request.values= ', request.values)
    print('request.url= ', request.url)
    print('request.host= ', request.host)
    print('request.charset= ', request.charset)
    print('request.range= ', request.range)
    print('request.blueprint= ', request.blueprint)
    print('request.base_url= ', request.base_url)

    # return Response(render_template('hello.html', name='tom'), status=200, content_type='text/html')
    return make_response(render_template('hello.html', name='nike'), 200)


@app.route('/redirect/')
def rdct():
    """
    重定向
    :return:
    """
    return redirect(url_for('get_phone'))


@app.route('/abort/')
def abort_resp():
    """
    直接中断返回
    :return:
    """
    # abort(404)
    abort(Response('Hello abort'))


@app.route('/json/')
def json_resp():
    """
    json响应
    :return:
    """
    # r = jsonify({'name': 'tom_dict', 'age': 20})
    r = jsonify(name='tom_kwages', age=31)
    return r


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    manager.run()  # python manager_1.py runserver -d -r -h 0.0.0.0 -p 5000
