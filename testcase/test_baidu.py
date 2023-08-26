# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : test_baidu.py
@Time     : 2023/8/26 14:30
@Author   : ShiWeiZheng
@Function :
"""
import allure

import allure
import pytest
import os


@allure.step("登录获取token")
def get_token():
    print("请求登录接口获取token")


@allure.step("加入购物车")
def add_to_shopping_trolley():
    print("请求加入购物车接口")


@allure.step("查询我的购物车")
def get_shopping_trolley_goods():
    print("请求查询我的购物车接口")


@allure.step("清空购物车")
def empty_shopping_trolley():
    print("请求清空购物车接口")


@allure.step("下单")
def place_order():
    print("请求下单接口")


@allure.epic("xx在线购物平台接口测试")
@allure.feature("购物车功能模块")
class testShoppingTrolley:

    @allure.story("商品加入购物车")
    @allure.title("正向用例--将库存数>0的商品加入购物车")
    @allure.description("校验库存数不为0的商品加入购物车是否正常")
    @allure.severity("critical")
    def test_add_goods(self):
        get_token()
        add_to_shopping_trolley()

    @allure.story("商品加入购物车")
    @allure.title("异常用例--将库存数=0的商品加入购物车")
    @allure.description("校验库存数为0的商品加入购物车是否提示正确的错误信息")
    @allure.severity("normal")
    def test_add_goods_error(self):
        get_token()
        add_to_shopping_trolley()

    @allure.story("查询购物车商品数量")
    @allure.title("查询购物车所有商品的总数量")
    @allure.description("校验查询购物车所有商品的总数量是否正常")
    @allure.severity("critical")
    def test_get_goods_quantity(self):
        get_token()
        add_to_shopping_trolley()
        get_shopping_trolley_goods()

    @allure.story("查询购物车商品数量")
    @allure.title("查询购物车单个商品的数量")
    @allure.description("校验查询购物车单个商品的数量是否正常")
    @allure.severity("critical")
    def test_get_goods_quantity(self):
        get_token()
        add_to_shopping_trolley()
        get_shopping_trolley_goods()

    @allure.story("清空购物车")
    @allure.title("加入商品后再清空购物车")
    @allure.description("校验清空购物车接口功能是否正常")
    @allure.severity("normal")
    def test_empty_shopping_trolley(self):
        get_token()
        add_to_shopping_trolley()
        empty_shopping_trolley()


@allure.epic("xx在线购物平台接口测试")
@allure.feature("下单模块")
class TestPlaceOrder:

    @allure.story("购物车下单")
    @allure.title("商品加入购物车再下单")
    @allure.description("校验清购物车下单功能是否正常")
    @allure.severity("critical")
    def test_place_order(self):
        get_token()
        add_to_shopping_trolley()
        place_order()

    @allure.story("立即购买下单")
    @allure.title("选择商品不加入购物车立即购买下单")
    @allure.description("校验立即购买下单功能是否正常")
    @allure.severity("critical")
    def test_order(self):
        get_token()
        place_order()
