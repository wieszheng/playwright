# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : config.py
@Time     : 2023/8/26 14:16
@Author   : ShiWeiZheng
@Function :
"""
import os


class Config:

    # 项目地址
    url = "http://124.223.40.245:83"
    EPIC = "大数据平台测试"

    # 项目根目录
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_PATH_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'logs'))
    TEST_CASE_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'testcase'))
    TEST_FILE_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'testfile'))
    TEST_DATA_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'testdata'))
    TEST_REPORT_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'testreport/allureReport'))
    TEST_RESULT_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'testreport/allureResult'))
    TEST_PIC_DIR = os.path.abspath(os.path.join(ROOT_PATH, 'pic'))

    # 浏览器
    BROWSER_TYPE = "chrome"

    # 日志名
    PW_ERROR = "pw_error"
    PW_INFO = "pw_info"


if __name__ == '__main__':
    print(Config.TEST_RESULT_DIR)