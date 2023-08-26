# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : runner.py
@Time     : 2023/8/26 14:11
@Author   : ShiWeiZheng
@Function :
"""
import os

import pytest

from conf.config import Config

if __name__ == '__main__':
    pytest.main(["-v", "-s", f"--alluredir={Config.TEST_RESULT_DIR}", "--clean-alluredir"])
    os.system(f'allure generate {Config.TEST_RESULT_DIR} -o {Config.TEST_REPORT_DIR} --clean')
