# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : assert.py
@Time     : 2023/8/26 19:12
@Author   : ShiWeiZheng
@Function :
"""
import re

from playwright.sync_api import expect


def wait_element_visibility(locator, timeout=15, poll=0.3, extra_wait=None):
    """
    等待元素可见(浏览器窗口显示范围内)
    :param extra_wait: 智能等待结束后的额外等待时间/秒
    :param locator: 元素定位信息
    :param timeout: 超时时间
    :param poll: 轮询间隔时间/秒
    :return:
    """
    pass


def custom_assert(condition, message):
    if not condition:
        raise AssertionError(message)


def assert_to_have_title(page):
    expect(page).to_have_title(re.compile(r".*checkout"))
