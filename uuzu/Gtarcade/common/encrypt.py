#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/27 15:45 
@Author : 乔乔 
@File : encrypt.py
:param 
:param 
:param 
'''
import hashlib


def md5(string):
	'''
	md5加密
	:param string: 待加密字符串
	:return: 已加密字符串
	'''
	md5 = hashlib.md5()  # 生成MD5对象
	md5.update(string.encode('utf-8'))  # 对数据加密,update点不出来，需要手动输入
	string_md5 = md5.hexdigest()  # 获取密文，hexdigest点不出来，需要手动输入
	print(string_md5)  # 输出加密后的数据

# md5('111111')