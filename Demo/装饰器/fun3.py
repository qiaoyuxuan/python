#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/30 15:18
author：乔誉萱
说明：装饰器的详解--被装饰函数有参数
:param 
:param 
'''

def login(func):
	def inner(username='qiao',pwd='123'):
		if username=='qiao' and pwd=='123':
			return func(username='qiao',pwd='123')
		else:
			return '登陆失败'
	return inner

@login
def homePage(username='qiao',pwd='123'):
	return '欢迎登陆首页！'

@login
def perManage(username='qiao',pwd='123'):
	return '欢迎进入人员管理！'
	
print(homePage(username='qiao',pwd='123'))
print(perManage(username='qiao1',pwd='123'))