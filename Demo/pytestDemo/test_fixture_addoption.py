#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/3 20:00
author：乔誉萱
说明：
读取conftest.py文件中的pytest_addoption注册命令行参数
:param 
:param 
'''
import pytest


def test_getFoo(getFoo,getUsername,getPasswd):
	'''三个参数就是conftest.py中的函数，返回他们的注册信息'''
	print('\n',getFoo)
	print(getUsername)
	print(getPasswd)


if __name__ == '__main__':
	# 没有指定值，则输出conftest.py中default中的默认值
	pytest.main(['-v','-s','test_fixture_addoption.py'])
	# 有默认值是，则输出默认值
	pytest.main(['-v','-s','test_fixture_addoption.py','--foo=我是指定值',
	             '--username=我是指定用户名','--passwd=‘我是指定密码'])
