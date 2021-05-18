#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/22 16:26 
@Author : 乔乔 
@File : get_params.py 读取fixtrue的参数化返回数据
:param 
:param 
:param 
'''

import pytest
from uuzu.app.Common import operationFile


@pytest.fixture(params=operationFile.read_Yaml(filedir='testData', filename='sdk_register.yml'))
def get_param_reg(request):
	'''返回sdk注册接口入参'''
	return request.param


@pytest.fixture(params=operationFile.read_Yaml(filedir='testData',filename='sdk_login.yml'))
def get_param_login(request):
	return request.param