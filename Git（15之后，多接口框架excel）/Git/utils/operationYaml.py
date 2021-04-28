#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/13 13:48
author：乔誉萱
说明：写入/读取/清空yaml文件
'''
import yaml,json
from common.public import filePath


class OperationYaml(object):
	@staticmethod
	def writeYaml(fileDir,fileName,wType,**kwargs):
		'''
		写入yaml文件
		:param fileDir: 文件路径
		:param fileName: 文件名称
		:param kwargs：写入内容
		:param wType：写入方式
		'''
		with open(filePath(fileDir=fileDir,fileName=fileName),wType,encoding='utf-8') as f:
			f.truncate()
			yaml.dump(data=kwargs,stream=f,allow_unicode=True)
	
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
	
	@staticmethod
	def cleanYaml(fileDir,fileName):
		'''
		清空yaml文件内容
		:param fileDir: 文件路径
		:param fileName: 文件名称
		'''
		with open(filePath(fileDir=fileDir,fileName=fileName),'w') as f:
			f.truncate()


if __name__ == '__main__':
	# r1 = OperationYaml.readYaml_list('data','pro_login.yml')
	# print(r1)
	# r2 = OperationYaml.readYaml_dict('config','apiFlowCase001.yaml')
	# print(r2)
	# w = {"case_002":{"code":0,"expireTime":"2020-11-19 13:54:32","jwtToken":"kfOWqFRK0","message":"success"}}
	# OperationYaml.writeYaml('data','response.yaml',w,'a')
	r3 = OperationYaml.readYaml_list('data','response.yaml')
	print(r3)
	# OperationYaml.cleanYaml(fileDir='data',fileName='response.yaml')
