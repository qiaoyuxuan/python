#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/3 13:13
author：乔誉萱
说明：fixture装饰器参数化案例
:param 
:param 
'''

import pytest

def add(a,b):
	return a + b

def datas():
	return [
	[2,2,4],
	[3,3,6],
	[4,4,8],
	[5,5,10]
]

@pytest.fixture(params=datas())
def getData(request):
	'''
	1、注意参数request为固定，不能自定义
	2、request.param点不出来，但必须用这个方法，否则后续无法通过getData[0]获取值
	'''
	return request.param


def test_param(getData):
	assert add(getData[0],getData[1]) == getData[2]
	

if __name__ == '__main__':
	pytest.main(['-v','-s','test_fixture_param.py'])
