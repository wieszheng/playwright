# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : logger.py
@Time     : 2023/8/26 16:02
@Author   : ShiWeiZheng
@Function :
"""
import inspect
import os

from loguru import logger

from conf.config import Config


class Log:
    business = None

    def __init__(self, name='PW'):  # Logger标识
        """
        :param name: 业务名称
        """
        # 如果目录不存在则创建
        if not os.path.exists(Config.LOG_PATH_DIR):
            os.mkdir(Config.LOG_PATH_DIR)
        self.business = name

    def info(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(inspect.currentframe().f_back)
        logger.bind(name=Config.PW_INFO, func=func, line=line,
                    business=self.business, filename=file_name).debug(message)

    def error(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(inspect.currentframe().f_back)
        logger.bind(name=Config.PW_ERROR, func=func, line=line,
                    business=self.business, filename=file_name).error(message)

    def warning(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(inspect.currentframe().f_back)
        logger.bind(name=Config.PW_ERROR, func=func, line=line,
                    business=self.business, filename=file_name).warning(message)

    def debug(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(inspect.currentframe().f_back)
        logger.bind(name=Config.PW_INFO, func=func, line=line,
                    business=self.business, filename=file_name).debug(message)

    def exception(self, message: str):
        file_name, line, func, _, _ = inspect.getframeinfo(inspect.currentframe().f_back)
        logger.bind(name=Config.PW_ERROR, func=func, line=line,
                    business=self.business, filename=file_name).exception(message)
