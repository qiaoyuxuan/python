#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/15 15:01
author：乔誉萱
说明：
:param 
:param 
'''
import os,yaml


def filePath(fileDir='data',fileName='terms_queryByPage.yaml'):
	'''
	获取指定文件路径
	:param fileDir:文件路径，data
	:param fileName:文件名称，默认terms_queryByPage.yaml
	:return:返回指定文件路径
	'''
	base_url = os.path.dirname(os.path.dirname(__file__))
	return os.path.join(base_url,fileDir,fileName)


def readYaml(fileDir='data',fileName='terms_queryByPage.yaml'):
	'''
	读取yaml文件
	:param fileDir: 文件路径，data
	:param fileName: 文件名称，默认terms_queryByPage.yaml
	:return: 返回yaml文件数据
	'''
	with open(filePath(fileDir,fileName),mode='r',encoding='utf-8') as f:
		return list(yaml.safe_load_all(f))

# print(readYaml(fileDir='data',fileName='terms_queryByPage.yaml'))
