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
from uuzu.Gtarcade.common import operationFile


@pytest.fixture(params=operationFile.read_yaml(filedir='testData', filename='pro_login.yml'))
def get_param_login(request):
	'''返回profile登录接口入参'''
	return request.param


@pytest.fixture(params=operationFile.read_yaml(filedir='testData', filename='pro_userInfo.yml'))
def get_param_info(request):
	'''返回profile用户信息接口入参'''
	return request.param


@pytest.fixture(params=operationFile.read_yaml(filedir='testData', filename='microapi_gamelist.yml'))
def get_param_gamelist(request):
	'''返回micro-api获取游戏中心列表接口入参'''
	return request.param


@pytest.fixture(params=operationFile.read_yaml(filedir='testData', filename='microapi_all_gamedetails.yml'))
def get_allparam_gamelist(request):
	'''返回micro-api获取游戏中心列表接口入参'''
	return request.param


if __name__ == '__main__':
	pytest.main(['-s', '-v', 'get_params.py'])
