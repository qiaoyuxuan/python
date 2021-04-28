#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/21 16:37 
@Author : 乔乔 
@File : operationFile.py 
:param 
:param 
:param 
'''
import yaml, os, string


def get_filePath(filedir, filename):
	'''
	获取指定文件路径
	:param filedir: 文件目录
	:param filename: 文件名称
	:return: 指定文件路径
	'''
	url = os.path.dirname(os.path.dirname(__file__))  # 获取目录的上一级
	return os.path.join(url, filedir, filename)  # 连接指定目录和文件夹名称


# print(get_filePath(filedir='testData',filename='pro_login.yml'))


def read_yaml(filedir, filename):
	'''
	读取指定的yaml文件,yaml文件有多条数据流
	:param filedir: 文件目录
	:param filename: 文件名称
	:return: 返回一个list
	'''
	with open(file=get_filePath(filedir=filedir, filename=filename), mode='r', encoding='utf-8') as f:
		return list(yaml.safe_load_all(f))


# print(read_yaml('testData', 'pro_login.yml'))


def write_yaml(filedir, filename, content):
	'''
	写入指定yaml文件，追加写入
	:param filedir: 文件目录
	:param filename: 文件名称
	:param content: 写入内容
	'''
	with open(file=get_filePath(filedir=filedir, filename=filename), mode='w', encoding='utf-8') as f:
		yaml.dump(data=content, stream=f, allow_unicode=True)

# def open_template_yaml(filedir, filename, data: dict):
# 	with open(file=get_filePath(filedir=filedir, filename=filename), encoding='utf-8') as f:
# 		cont = string.Template(f.read()).safe_substitute(data)
# 		print(yaml.safe_load(cont))
#
#
# set_data = {'game_id':'[1,2,3]'}
# open_template_yaml(filedir='testData', filename='microapi_gamelist.yml', data=set_data)
