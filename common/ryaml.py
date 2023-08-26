# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : ryaml.py
@Time     : 2023/8/26 18:03
@Author   : ShiWeiZheng
@Function :
"""
import os
import yaml
from conf.config import Config


def read(yamlFile):
    path = os.path.abspath(os.path.join(Config.TEST_DATA_DIR, yamlFile))
    f = open(path, mode='r', encoding='utf8')
    return yaml.safe_load(f)
