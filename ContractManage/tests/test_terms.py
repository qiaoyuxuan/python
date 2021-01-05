#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/15 10:11
author：乔誉萱
说明：获取条款列表
:param 
:param 
'''

from base.method import Requests
from common.getFixture import *

obj_request = Requests()


@pytest.mark.skip(reason='忽略新增条款用例')
def test_submit(getData_submit,conftest_getHeaders):
	'''
	测试用例：新增条款
	:param getData_submit: fixture装饰器返回yaml数据集--新增条款（在fixtureData目录下）
	:param conftest_getHeaders: conftest.py模块返回的请求头
	'''
	result = obj_request.post(
		url=getData_submit['url'],
		headers=conftest_getHeaders,
		json=getData_submit['data']
	)
	assert getData_submit['message'] == result.json()['message']
	return result.json()


@pytest.mark.skip(reason='忽略获取条款信息用例')
@pytest.fixture()
def test_queryByPage(getData_queryByPage,conftest_getHeaders):
	'''
	测试用例：获取条款列表
	:param getData_queryByPage: fixture装饰器返回yaml数据集-条款列表（在fixtureData目录下）
	:param conftest_getHeaders: conftest.py模块返回的请求头
	:return: 返回接口返回数据--条款列表
	'''
	listData = []
	result = obj_request.post(
		url=getData_queryByPage['url'],
		headers=conftest_getHeaders,
		json=getData_queryByPage['data']
	)
	# print(result.json())
	assert result.json()['message'] == getData_queryByPage['message']  # 断言message
	for i in range(0,result.json()['pageSize']):
		assert result.json()['data'][i]['status'] == getData_queryByPage['data']['status']  # 断言审核类型
	if getData_queryByPage['data']['status'] == 0:  # 判断当获取的数据集中，审核状态为0待审核时
		listData = result.json()['data']  # 将接口返回的待审核条款放入list中并返回
	# print(listData)
	return listData


def test_modify(getData_modify,conftest_getHeaders):
	'''
	条款修改
	:param getData_queryByPage: fixture装饰器返回yaml数据集-条款列表（在fixtureData目录下）
	:param conftest_getHeaders: conftest.py模块返回的请求头
	:param test_queryByPage: test_queryByPage接口返回“待审核”状态数据集
	:return:
	'''
	'''判断获取的yaml数据中data==${code}时，则赋值条款code，根据code进行修改'''
	if getData_modify['data']['code'] == '${code}':
		getData_modify['data']['code']='3f514be227c943fabfe7f240900fd455'
	
	result = obj_request.post(
		url=getData_modify['url'],
		headers=conftest_getHeaders,
		json=getData_modify['data']
	)
	# print(result.json())
	assert result.json()['message']==getData_modify['message']


if __name__ == '__main__':
	pytest.main(['-v','-s','test_terms.py'])
