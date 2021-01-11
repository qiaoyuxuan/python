#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/11 17:48
author：乔誉萱
说明：
1、判断字符串内是否有重复字符，使用set集合
:param 
:param 
'''

def setStr(str1):
	'''
	判断字符串内是否有重复字符
	思路：
	1、使用set集合，可以去除字符串内重复字符
	2、然后对比set前后的字符串长度即可，长度有变化则代表有重复字符，反之则无
	'''
	if len(str1) == len(set(str1)):
		return '无重复字符'
	else:
		return '有重复字符'


str1 = 'Hello'
print(setStr(str1))