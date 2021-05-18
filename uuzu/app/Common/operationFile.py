#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/23 16:09 
@Author : 乔乔 
@File : operationFile.py 
操作文件
'''

import yaml, os



def get_filePath(filedir, filename):
	'''
	获取指定文件路径
	:param filedir: 文件目录
	:param filename: 文件名称
	:return: 指定文件路径
	'''
	url = os.path.dirname(os.path.dirname(__file__))  # 获取目录的上一级
	return os.path.join(url, filedir, filename)  # 连接指定目录和文件夹名称

# print(get_filePath(filedir='testData',filename='sdk_register.yml'))


def read_Yaml(filedir, filename):
	'''
	读取file文件夹下的login_sign.yaml文件数据，并返回一个dict
	:return:
	'''
	with open(file=get_filePath(filedir=filedir, filename=filename), mode='r', encoding='utf-8') as f:
		return yaml.safe_load(f)


# print(read_Yaml(filedir='testData',filename='sdk_register.yml'))


