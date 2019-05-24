#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 10:23
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : views.py
# @Software: PyCharm
import sys
from flask import Blueprint, Flask, request, render_template, current_app, abort, g
import random

from sqlalchemy import and_, or_, not_

from qff.App.ext import db
from qff.App.models import User, Product, Customer, CompanyShop

bp = Blueprint('first_bp', __name__)


def init_bp(*, app: Flask):
    """
    初始化 blueprint
    :param app:
    :return:
    """
    app.register_blueprint(blueprint=bp)


@bp.route('/')
def index():
    return 'hello flask'


@bp.route('/adduser/')
def add_user():
    """
    添加用户
    :return:
    """
    random_int = random.randint(100, 200)
    user = User(f'Tom{random_int}', f'123{random_int}')

    db.session.add(user)
    db.session.commit()

    return 'add user success'


@bp.route('/addproduct/')
def add_product():
    """
    添加产品
    :return:
    """
    user = User.query.order_by(User.id.desc()).first()

    random_int = random.randint(100, 300)
    product = Product(name=f'电脑X{random_int}', price=f'{random_int * 100}', user_id=user.id)

    db.session.add(product)
    db.session.commit()

    return 'add product success'


@bp.route('/getusers/')
@bp.route('/userlist/')
def get_users():
    """
    获取用户列表
    :return:
    """
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)

    # 分页器
    # pagination = db.session.query(User).paginate(page=page, per_page=per_page)
    pagination = User.query.paginate(page=page, per_page=per_page)
    # users = pagination.items  # 直接获取分页数据集

    # 手动分页
    # users = db.session.query(User).offset((page - 1) * per_page).limit(per_page)

    # User表所有数据
    # users = User.query.all()
    # users = db.session.query(User).all()

    # 读取id>=10的数据 __gt__ __lt__ __ge__ __le__
    # users = User.query.filter(User.id >= 10)

    # 筛选username='Tom2'的数据
    # users = User.query.filter_by(username='Tom2')

    # 读取username中包含"1"的数据
    # users = User.query.filter(User.username.contains('1'))

    # 读取username中以"Tom1"开始的数据
    # users = User.query.filter(User.username.startswith('Tom1'))

    # 按照username排序，跳过2条，长度为5
    # users = User.query.order_by("username").offset(2).limit(5)

    # 模糊查询 like
    # users = User.query.filter(User.username.like('%1%'))

    # and or in not
    # users = User.query.filter(User.id.in_([1, 3, 5, 7]))
    # users = User.query.filter(and_(User.id > 5, User.id < 20))
    # users = User.query.filter(or_(User.id <= 5, User.id >= 20))
    # users = User.query.filter(not_(User.id == 5))

    # for u in users:
    #     print(u.id)

    return render_template('user_list.html', pagination=pagination)


@bp.route('/getuser/')
def get_user():
    """
    获取用户
    :return:
    """
    # 获取id=10的数据
    # u = User.query.get(10)

    # 获取User表最后一条数据（先按照id倒序，再取第一条）
    u = db.session.query(User).order_by(User.id.desc()).first()

    return f'{u.id}\t{u.username}\t{u.password}'


@bp.route('/getuserbyproduct/')
def get_user_by_product():
    """
    通过产品获取所属用户
    :return:
    """
    # 获取产品列表最新一条数据所属的用户
    product = Product.query.order_by(Product.id.desc()).first()

    # User模型中加入与Product级联关系，无需手动关联查询user，可直接获取（懒加载，自动查询）
    # user = User.query.get(product.user_id)
    user = product.user

    print(product.id, product.name, product.price, product.user_id, sep='\t')
    print(user.id, user.username, user.password, sep='\t')

    return 'get user by product success'


@bp.route('/getproductsbyuser/')
def get_products_by_user():
    """
    通过用户获取所拥有的产品
    :return:
    """
    # 获取最新用户所拥有的产品
    user = User.query.order_by(User.id.desc()).first()

    # User模型中加入与Product级联关系，无需手动关联查询products，可直接获取（懒加载，自动查询）
    # products = Product.query.filter(Product.user_id == user.id).all()
    products = user.products

    return render_template('products.html', products=products)


@bp.route('/getconfiglist/')
def get_config_list():
    """
    获取全局属性config
    :return:
    """
    # _config = current_app.config
    # print(type(_config))
    # print(_config)

    print(g.get('temp'))
    return render_template('config_list.html')


@bp.route('/getcustomerfocusshop/')
def get_customer_focus_shop():
    """
    获取用户关注的商铺
    :return:
    """
    customer = Customer.query.get(1)
    focus_shops_list = customer.focus_shops
    return render_template('customer_focus_shops.html', shops=focus_shops_list)


@bp.route('/getshopfollowers/')
def get_shop_followers():
    """
    获取商铺的关注者
    :return:
    """
    shop = CompanyShop.query.get(4)
    followers_list = shop.followers
    return render_template('shop_followers.html', followers=followers_list)


@bp.route('/addfocusshop/')
def add_focus_shop():
    """
    添加新的关注店铺
    :return:
    """
    # cstm_1 = Customer(wx_openid='0000000004', phone_number='13812340004')
    # cstm_2 = Customer(wx_openid='0000000005', phone_number='13812340005')
    # cstm_3 = Customer.query.get(1)
    #
    # shop_1 = CompanyShop(shop_name='商铺名称4', company_name='商铺公司4')
    # shop_2 = CompanyShop(shop_name='商铺名称5', company_name='商铺公司5')
    # shop_3 = CompanyShop.query.get(2)

    cstm_1 = Customer.query.get(1)
    cstm_2 = Customer.query.get(4)
    cstm_3 = Customer.query.get(5)

    shop_1 = CompanyShop.query.get(2)
    shop_2 = CompanyShop.query.get(4)
    shop_3 = CompanyShop.query.get(5)

    cstm_1.focus_shops.append(shop_1)
    cstm_1.focus_shops.append(shop_2)
    cstm_1.focus_shops.append(shop_3)

    cstm_2.focus_shops.append(shop_1)
    cstm_2.focus_shops.append(shop_3)

    cstm_3.focus_shops.append(shop_1)

    db.session.add(cstm_1)
    db.session.add(cstm_2)
    db.session.add(cstm_3)

    db.session.commit()

    return '添加新的关注店铺成功'


@bp.before_app_first_request
def before_app_first_request_func():
    """
    应用第一次请求前执行
    :return:
    """
    print('before_app_first_request')


@bp.before_app_request
def before_app_request_func():
    """
    应用请求前执行
    :return:
    """
    print('before_app_request')


@bp.before_request
def before_request_func():
    """
    蓝图请求前执行
    :return:
    """
    g.temp = '-- data from g --'
    print('before_request')


@bp.after_request
def after_request_func(response):
    """
    蓝图请求后执行（如果请求没有异常）
    :return:
    """
    print('after_request')
    return response


@bp.after_app_request
def after_app_request(response):
    """
    应用请求后执行（如果请求没有异常）
    :return:
    """
    print('after_app_request')
    return response


@bp.teardown_request
def teardown_request_func(e):
    """
    蓝图请求后执行（即是请求没有异常）
    :return:
    """
    print('teardown_request', e)


@bp.teardown_app_request
def teardown_app_request_func(e):
    """
    应用请求后执行（即是请求没有异常）
    :return:
    """
    print('teardown_app_request', e)
