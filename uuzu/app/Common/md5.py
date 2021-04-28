#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/24 10:24 
@Author : 乔乔 
@File : encrypt.py
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
	sign = hashlib.md5(bytes(str(string), encoding='utf-8'))  # 对数据加密
	return sign.hexdigest()  # 获取密文，hexdigest点不出来，需要手动输入


print(get_md5('loginTs=1618318177&nickname=&token=5ae3027f4b755395472aa0c9332de5a2&username=353920114@qq.common&uuid=1596092549336910522297673z1QO9g&qD@7HetV6'))
