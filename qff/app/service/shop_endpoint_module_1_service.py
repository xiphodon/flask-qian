#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 16:42
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : shop_endpoint_module_1_service.py
# @Software: PyCharm
from qff.app.models.models import Customer


class ShopModuleService:
    """
    商户端某模块业务
    """
    def get_customer_focus_shop(self, customer_id: int):
        """
        获取c用户关注的商铺
        :param customer_id:
        :return:
        """
        customer = Customer.query.get(customer_id)
        if customer:
            focus_shops_list = customer.focus_shops
        else:
            focus_shops_list = []
        return customer, focus_shops_list
