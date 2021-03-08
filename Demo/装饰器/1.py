#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/30 9:45
author：乔誉萱
说明：函数的应用范围
:param
:param
'''


# 函数可以当做一个变量：下面f即是引用fun1()函数的变量---------------------------------------------------------------
def fun1():
	return 'hello'


f = fun1()
print(f)

# 函数可以当做一个参数：下面profile函数的参数就是login函数，profile使用login的返回值作为参数-------------------------
def login(username='qiao',password='123'):
	if username == 'qiao' and password == '123':
		return 'akjfkajflkj'
	else:
		return '登陆失败'


def profile(token):
	if token == 'akjfkajflkj':
		return '欢迎访问主页！'
	else:
		return 'token失效！'


print(profile(login()))  # 输出：欢迎访问主页！
print(profile(login(username='qiao',password='1')))  # 输出：token失效！

# 函数可以嵌套：下面fun3()中嵌套了fun4()，在fun3中返回fun4的返回值-------------------------------------------------
def fun3():
	def fun4():
		return '我是fun4()函数的返回值'
	return fun4()
print(fun3())
