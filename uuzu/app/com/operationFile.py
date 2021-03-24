#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/23 16:09 
@Author : 乔乔 
@File : operationFile.py 
操作文件
'''

import yaml
from uuzu.app.com import get_path  # 获取文件路径的模块


def read_Yaml(dirname):
	'''
	读取file文件夹下的login_sign.yaml文件数据，并返回一个dict
	:return:
	'''
	with open(get_path.get_dir(dirname), 'r', encoding='utf-8') as f:
		return yaml.safe_load(f)

# print(read_Yaml('app/file/login_sign.yaml'))
