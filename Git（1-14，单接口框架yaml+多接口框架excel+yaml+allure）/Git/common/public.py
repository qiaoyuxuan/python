#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/13 13:38
author：乔誉萱
说明：获取文件路径
'''
import os


def filePath(fileDir,fileName):
	'''
	获取文件路径
	:param fileDir: 文件目录
	:param fileName: 文件名称
	:return: 返回文件路径
	'''
	base_url = os.path.dirname(os.path.dirname(__file__))
	return os.path.join(base_url,fileDir,fileName)


def writeFile(writeCentent):
	'''
	写入文件
	:param writeCentent: 写入文件内容
	'''
	with open(filePath(fileDir='data',fileName='returnData.json'),'w',encoding='utf-8') as f:
		f.write(writeCentent)


def readFile(fileDir='data',fileName='returnData.json'):
	'''
	读取文件
	:return: 返回读取内容
	'''
	with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
		return f.read()


'''测试'''
# print(filePath('data','login.yaml'))
writeFile('测试')
# print(readFile())
