#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/5/17 14:59 
@Author : 乔乔 
@File : test_sdk.py app注册接口，注册200个账号供云测使用
:param 
:param 
:param 
'''

from uuzu.app.Common import sign, method, operationFile
from uuzu.app.Common.get_params import get_param_reg, get_param_login
import pytest, requests, allure

request = method.Requests()


@allure.title('sdk注册接口,生成200个账号注册')
# @pytest.mark.skip(reason='跳过该用例')
def test_sdk_register_200():
	get_param = operationFile.read_Yaml(filedir='testData', filename='sdk_register.yml')  # 获取接口参数
	list_name = sign.reg_name(username=get_param['data']['username'], range_start=30, range_end=150)  # 获取所有待注册的用户名
	'''
	循环注册200个用户，每次循环后需重置用户名、重置密码、删除sign，才能将字符串再次加密为新的sign并赋值给sign
	'''
	for i in range(len(list_name)):
		# print(list_name[i])
		get_param['data']['username'] = list_name[i]  # 循环赋值用户名
		get_param['data']['password'] = '111111'  # 重设密码（因为第一次循环后密码被加密）
		get_param['data']['sign'] = sign.get_reg_sign(get_param['data'], 'android')  # 赋值加密后的sign值
		# print(get_param['data']['username'])

		response = request.post(url=get_param['url'], headers=get_param['headers'], data=get_param['data'])
		print(response.json())
		assert response.json()['desc'] == get_param['expect']['desc']
		del get_param['data']['sign']  # 删除sign，每注册完一个需删除，否则sign会被放入加密串，生成是新sign就是错的


@allure.title('sdk登录接口')
@pytest.mark.skip(reason='跳过该用例')
def test_login():
	get_login_param = operationFile.read_Yaml(filedir='testData', filename='sdk_login.yml')
	print(get_login_param)
	list_name = sign.reg_name(username=get_login_param['data']['username'], range_start=1, range_end=29)  # 获取所有待注册的用户名
	print(list_name)
	for i in range(len(list_name)):
		get_login_param['data']['username'] = list_name[i]
		get_login_param['data']['sign']=sign.get_login_sign()
		response = request.post(url=get_param_login['url'], data=get_login_param['data'])
		print(response.json())
		assert response.json()['desc'] == get_login_param['expect']['desc']


if __name__ == '__main__':
	pytest.main(['-v', '-s', 'test_sdk.py'])
