# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : dallure.py
@Time     : 2023/8/26 17:37
@Author   : ShiWeiZheng
@Function :
"""
import functools
import os

import allure
import pytest
from conf.config import Config


class Allure:

    @classmethod
    def AllureCase(cls, page, CaseData):
        """动态设置allure"""
        allure.dynamic.epic(Config.EPIC)
        allure.dynamic.feature(CaseData.get("模块"))
        allure.dynamic.story(CaseData.get("功能"))
        allure.dynamic.severity(CaseData.get("优先级"))
        allure.dynamic.title(CaseData.get("用例标题"))
        allure.dynamic.description(CaseData.get("用例描述"))
        if CaseData.get("是否执行") != "Y":
            allure.dynamic.description("用例指定跳过")
            pytest.skip("用例指定跳过")

    @classmethod
    def AllureScreenShot(cls, page, CaseData):
        filename = os.path.join(Config.TEST_PIC_DIR, f"{CaseData.get('用例标题')}.png")
        page.screenshot(path=filename)
        allure.attach.file(source=filename, name=CaseData.get('用例标题'), attachment_type=allure.attachment_type.PNG)

    @classmethod
    def AllureWarpper(cls, func):
        """装饰器函数"""

        @functools.wraps(func)
        def inner(*args, **kwargs):
            # 添加用例信息
            cls.AllureCase(page=kwargs.get("page"), CaseData=kwargs.get("CaseData"))  # 如何获取case_data?
            r = func(*args, **kwargs)  # 运行用例
            # 添加截图
            cls.AllureScreenShot(page=kwargs.get("page"), CaseData=kwargs.get("CaseData"))
            return r

        return inner
