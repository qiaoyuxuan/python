#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/24 10:24 
@Author : 乔乔 
@File : md5.py 
:param 
:param 
:param 
'''
import hashlib


def get_md5(string):
	'''
	MD5加密
	:param string: 待加密字符串
	:return: 加密后的字符串
	'''
	sign = hashlib.md5(bytes(string,encoding='utf-8'))  # 对数据加密
	return sign.hexdigest()  # 获取密文，hexdigest点不出来，需要手动输入

# print(get_md5('aaa'))