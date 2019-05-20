#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:17
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : manager.py
# @Software: PyCharm
from pathlib import Path
import sys

from flask_migrate import MigrateCommand
from flask_script import Manager

base_path = str(Path(__file__).resolve().parent.parent)
# print(base_path)
if base_path not in sys.path:
    sys.path.append(base_path)

from qff.App import create_app


app = create_app()
manager = Manager(app=app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
