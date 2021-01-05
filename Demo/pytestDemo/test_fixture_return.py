#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/26 11:00
author：乔誉萱
说明：fixture装饰器返回值案例
:param 
:param 
'''
import pytest

@pytest.fixture()
def fixData():
	return 'hello'

def test_fixture(fixData):
	'''参数为装饰器下的函数，则可以获取装饰器返回值'''
	assert fixData=='hello'

if __name__ == '__main__':
	pytest.main(['-s','-v','test_fixture_return.py'])

