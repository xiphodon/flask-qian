#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 16:38
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : shop_endpoint_module_1.py
# @Software: PyCharm

"""
商户端 模块1
"""
from flask import Blueprint, url_for, jsonify, request
from qff.app.service.shop_endpoint_module_1_service import ShopModuleService
from qff.app.utils.request_utils import switch_method

bp = Blueprint('api_v1_bp', __name__, url_prefix='/api/v1')


@bp.route('/customer/<int:customer_id>/focusshops/', methods=['GET'])
def get_customer_focus_shops(customer_id):
    """
    获取某个c用户关注的商铺
    :param customer_id:
    :return:
    """

    shop_module_service = ShopModuleService()
    customer, customer_focus_shop = shop_module_service.get_customer_focus_shop(customer_id=customer_id)

    data = dict()
    if customer:
        data = {
            'customer_id': customer.id,
            'phone_number': customer.phone_number,
            'focus_shop': [{
                'shop_id': shop.id,
                'shop_name': shop.shop_name,
                'company_name': shop.company_name
            } for shop in customer_focus_shop]
        }

    return jsonify(data)


@bp.route('/CustomerFocusShop/', methods=['POST'])
def post_customer_focus_shop():
    """
    获取某个c用户关注的商铺
    :param customer_id:
    :return:
    """
    name = request.form.get('name')
    age = request.form.get('age')

    return jsonify({'name': name, 'age': age})
