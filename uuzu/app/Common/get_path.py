#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/23 16:24 
@Author : 乔乔 
@File : get_path.py
'''

import os


def get_dir(path):
	'''
	返回到指定目录
	:param path:拼接的目录
	:return:返回到uuzu目录
	'''
	dir_name = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), path)
	# print(dir_name)
	return dir_name


get_dir('')
