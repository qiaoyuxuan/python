#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/21 16:29 
@Author : 乔乔 
@File : test_profile.py
:param 
:param 
:param 
'''
from uuzu.Gtarcade.common.method import Requests
from uuzu.Gtarcade.common.get_params import *

import pytest, allure

obj_request = Requests()


@allure.title('profile登录接口')
def test_login(conf_getCookie):
	assert conf_getCookie != ''


@allure.title('profile用户信息接口')
def test_userInfo(conf_getCookie, get_param_info):
	'''
	profile用户信息接口
	:param conf_getCookie:登录接口返回的cookie
	:param get_param_info:fixture返回，profile用户信息接口的入参（yaml文件）
	'''
	get_param_info['header']['Cookie'] = conf_getCookie  # cookie赋值
	# print(type(get_param_info))
	response = obj_request.post(url=get_param_info['url'],
	                            headers=get_param_info['header'])

	# print(response.json())
	assert response.json()['status'] == get_param_info['expect']['status']
	assert response.json()['msg'] == get_param_info['expect']['msg']


if __name__ == '__main__':
	pytest.main(
		['-s', '-v', '--lf', 'test_profile.py', '--alluredir=../allure-report/profile/result', '--clean-alluredir'])
	import subprocess

	# subprocess.call('allure generate ../allure-Report/profile/result/ -o ../allure-Report/profile/html --clean',
	#                 shell=True)
	# subprocess.call('allure open -h 127.0.0.1 -p 8089 ../allure-Report/profile/html', shell=True)
