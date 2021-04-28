#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/13 13:48
author：乔誉萱
说明：读取yaml文件
'''
import yaml
from common.public import filePath


class OperationYaml(object):
	@staticmethod
	def readYaml_list(fileDir,fileName):
		'''静态读取yaml文件，调用自定义filePath方法获取对应yaml文件
		:param fileDir: 文件路径
		:param fileName: 文件名称
		:return: 返回yaml文件内容，类型list
		'''
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding="utf-8") as f:
			return list(yaml.safe_load_all(f))
	
	@staticmethod
	def readYaml_dict(fileDir,fileName):
		'''静态读取yaml文件，调用自定义filePath方法获取对应yaml文件
		:param fileDir: 文件路径
		:param fileName: 文件名称
		:return: 返回读取内容，类型dict
		'''
		with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
			return yaml.safe_load(f)


if __name__ == '__main__':
	# r1 = OperationYaml.readYaml_list('data','pro_login.yml')
	# print(r1)
	r2 = OperationYaml.readYaml_dict('config','apiFlowCase001.yaml')
	print(r2['case_005'])
