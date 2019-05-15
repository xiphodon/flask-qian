#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 16:22
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : manager.py
# @Software: PyCharm
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app=app)


@app.route('/hello/')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=5000)
    manager.run()  # python manager.py runserver -d -r -h 0.0.0.0 -p 5000
