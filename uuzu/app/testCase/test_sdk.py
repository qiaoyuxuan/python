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
from uuzu.app.Common.get_params import get_param_reg
import pytest, requests, allure

request = method.Requests()


@allure.title('sdk注册接口,生成200个账号注册')
def test_sdk_register_200():
	get_param = operationFile.read_Yaml(filedir='testData', filename='register_sign.yml')  # 获取接口参数
	list_name = []
	list_name = sign.reg_name(username=get_param['data']['username'],num=3)  # 获取所有待注册的用户名
	'''
	循环注册200个用户，每次循环后需重置用户名、重置密码、删除sign，才能将字符串再次加密为新的sign并赋值给sign
	'''
	for i in range(len(list_name)):
		# print(list_name[i])
		get_param['data']['username'] = list_name[i]  # 循环赋值用户名
		get_param['data']['password'] = '111111'      # 重设密码（因为第一次循环后密码被加密）
		get_param['data']['sign'] = sign.get_sign(get_param['data'], 'android')  # 赋值加密后的sign值
		# print(get_param['data']['username'])
		# print(get_param['data']['sign'])

		response = request.post(url=get_param['url'], headers=get_param['headers'], data=get_param['data'])
		print(response.json())
		assert response.json()['desc'] == get_param['expect']['desc']
		del get_param['data']['sign']  # 删除sign，每注册完一个需删除，否则sign会被放入加密串，生成是新sign就是错的


if __name__ == '__main__':
	pytest.main(['-v', '-s', 'test_sdk.py'])
