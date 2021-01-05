#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/26 16:48
author：乔誉萱
说明：fixture装饰器初始化与清理案例
:param 
:param 
'''
import pytest


def add():
	print('\n我是添加')


def delete():
	print('我是删除')


@pytest.fixture()
def init():
	add()
	'''
	yield可以当做一个return，跟return不同的是，他是一个迭代器，下一次迭代开始的地方是从上一次迭代停止的地方开始执行
	所以在test_001调用init()函数时，会先执行add()函数，然后返回执行自己(即test_001)，最后再接着执行init()中的delete()函数
	'''
	yield
	delete()


def test_001(init):
	print('我是测试用例001，查看')


if __name__ == '__main__':
	pytest.main(['-v','-s','test_fixture_init.py'])
