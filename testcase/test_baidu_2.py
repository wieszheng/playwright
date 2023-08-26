# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : test_baidu_2.py
@Time     : 2023/8/26 17:17
@Author   : ShiWeiZheng
@Function :
"""

import pytest

from common.dallure import Allure
from common.ryaml import read
from page.baidupage import BaiduPage


class test_openbaidu:
    @pytest.mark.run(order=2)
    @Allure.AllureWarpper
    @pytest.mark.parametrize("CaseData", read("test_baidu_2.yaml"))
    def test_baidu(self, page, CaseData):
        new_page = BaiduPage(page)
        new_page.goto_login(CaseData["url地址"])

    @pytest.mark.run(order=1)
    @Allure.AllureWarpper
    @pytest.mark.xfail(raises=ZeroDivisionError)
    @pytest.mark.parametrize("CaseData", read("test_baidu_2.yaml"))
    def test_baidu_1(self, page, CaseData):
        new_page = BaiduPage(page)
        new_page.goto_login(CaseData["url地址"])


if __name__ == '__main__':
    pytest.main()
