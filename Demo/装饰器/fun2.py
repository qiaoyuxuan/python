#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/30 10:43
author：乔誉萱
说明：装饰器的详解--被装饰函数无参数
:param 
:param 
'''

'''编写代码的2个原则：
封装：对已实现的功能代码尽可能的不要改动
开放：对已实现的功能代码可以扩展
'''

'''
装饰器说明：
	当被装饰函数f1引用装饰函数getInfo时，f1就是getInfo函数的参数，所以装饰函数getInfo必须带有参数
需求：
	当调用f1 or f2函数时，先打印“我是已实现的fun函数！”，再打印“我是扩展的XX函数！”
调用顺序：
	1、当执行到f1()时，首先执行其装饰函数getInfo，并将f1作为参数传入getInfo，此时打印出：我是已实现的fun函数！
	2、继续执行inner函数中的func()时（func是形参，实际指向的是f1函数），则跳转到f1函数中执行
	3、将f1函数执行结果重新赋值给inner函数并返回
'''

def getInfo(func): # 3
	def inner():
		print('我是已实现的fun函数！') # 4
		func() # 5 / 7
	return inner

@getInfo # 2
def f1():
	print('我是扩展的f1函数！') # 6

@getInfo
def f2():
	print('我是扩展的f2函数！')


f1()  # 1
f2()
# f1()等价于getInfo(f1())
getInfo(f1())