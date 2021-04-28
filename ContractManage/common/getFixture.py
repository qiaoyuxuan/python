#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/15 20:28
author：乔誉萱
说明：fixture装饰器集中封装
'''

import pytest
from common import public


@pytest.fixture(params=public.readYaml(fileDir='data',fileName='terms_submit.yaml'))
def getData_submit(request,conftest_getHeaders):
	'''返回yaml数据——新增条款'''
	return request.param


@pytest.fixture(params=public.readYaml(fileDir='data',fileName='terms_queryByPage.yaml'))
def getData_queryByPage(request):
	'''返回yaml数据——获取条款列表'''
	return request.param


@pytest.fixture(params=public.readYaml(fileDir='data',fileName='terms_modify.yaml'))
def getData_modify(request):
	'''返回yaml数据——修改条款'''
	return request.param

def test_param(getData_submit):
	print(getData_submit[0])

if __name__ == '__main__':
	pytest.main(['-v','-s','getFixture.py'])