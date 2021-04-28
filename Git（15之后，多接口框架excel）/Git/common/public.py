#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/13 13:38
author：乔誉萱
说明：获取文件路径
'''
import os,json


def filePath(fileDir,fileName):
	'''
	获取文件路径
	:param fileDir: 文件目录
	:param fileName: 文件名称
	:return: 返回文件路径
	'''
	base_url = os.path.dirname(os.path.dirname(__file__))
	return os.path.join(base_url,fileDir,fileName)


def writeFile(writeCentent,wType,fileDir,fileName):
	'''
	写入文件
	:param writeCentent: 写入文件内容
	:param wType：写入方式
	:param fileDir：文件目录
	:param fileName：文件名称
	'''
	with open(filePath(fileDir=fileDir,fileName=fileName),wType,encoding='utf-8') as f:
		f.write(writeCentent)


def readFile(fileDir,fileName):
	'''
	读取文件
	:param fileDir：文件目录
	:param fileName：文件名称
	:return: 返回读取内容
	'''
	with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
		return f.read()


def traverse_take_field(data,fields,values=[],current_key=None):
	'''
	查询多个key在指定数据类型中是否存在，存在则返回该key和value
	:param data: 要遍历的数据类型，支持嵌套的dict和list
	:param fields: 要查找的字段
	:param values: 存放查到到的key和value
	:param current_key: 每次要遍历的key
	:return: 查找到的key和value，存放在list中返回
	'''
	if isinstance(data,list):  # 判断data是否为list类型
		for i in data:  # 遍历list
			traverse_take_field(i,fields,values,current_key)  # 将list放入并递归判断list
	elif isinstance(data,dict):  # 判断data是否为dict类型
		for key,value in data.items():  # 遍历dict，使用items()函数
			traverse_take_field(value,fields,values,key)  # 将dict放入并递归判断dict
	elif current_key in fields:  # 当data不是list或dict时，判断当前key是否存在与指定字段
		values.append(current_key)  # key和value放入list中
		values.append(data)
	return values  # 返回list


def list_to_dict(list_data):
	'''
	将list转为dict，注意：key不能重复，否则转换出来的dict不对
	:param list_data: 要转换的list
	:return: dict数据类型
	'''
	get_dict = dict(zip(list_data[0::2],list_data[1::2]))
	return get_dict


'''测试'''
# print(filePath('data','pro_login.yml'))
# writeFile('case001:\n'+str(w)+'\n',"a")

'''测试traverse_take_field'''
# dict_test = {'case_001': {'code': 0, 'expireTime': '2020-11-20 19:11:13', 'jwtToken': 'eyJhbGcik', 'message': 'success'},
# 	       'case_002': {'code': 0, 'expireTime': '2020-11-20 19:11:13', 'jwtToken1': 'eyJhbGcik', 'message': 'success'}}
# set_fields = ["jwtToken"]
# result_list = traverse_take_field(dict_test,set_fields)
# print(result_list)
# # result_dict = list_to_dict(result_list)
# # print("转为dict：", result_dict)