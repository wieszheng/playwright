# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : baidupage.py
@Time     : 2023/8/26 17:13
@Author   : ShiWeiZheng
@Function :
"""
import allure

from .basepage import Basepage


class BaiduPage(Basepage):
    # 元素定位器
    __username = "#username"
    __password = "#password"
    __verify_code = "#verify_code"
    __login_button = 'a[name="sbtbutton"]'
    __button_logout = 'a[title="退出"]'

    @allure.step("打开页面")
    def goto_login(self, url):
        self._goto_url(url)
