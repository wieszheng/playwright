# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : __init__.py.py
@Time     : 2023/8/26 15:55
@Author   : ShiWeiZheng
@Function :
"""
from common.logger import Log


class LogWrapper:

    def __init__(self, model, log=None):
        self.__model__ = model
        if log is None:
            self.__log__ = Log(f"{model.__name__}")
        else:
            self.__log__ = log

    def __call__(self, cls):
        setattr(cls, "__model__", self.__model__)
        setattr(cls, "__log__", self.__log__)
        return cls
