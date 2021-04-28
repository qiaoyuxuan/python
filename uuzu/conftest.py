#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/22 16:23 
@Author : 乔乔 
@File : conftest.py 
:param get_cookie函数：返回profile登录接口的cookie
:param 
:param 
'''

from uuzu.Gtarcade.common.get_params import get_param_login
from uuzu.Gtarcade.common import encrypt, method
import pytest

obj_request = method.Requests()  # 初始化类


@pytest.fixture()
def conf_getCookie(get_param_login):  # get_param_login参数为fixture函数，返回读取到的yaml文件数据
	'''
	profile登录接口，将返回的cookie重新拼接，返回拼接后的cookie，供其他接口使用
	:param get_param_login: fixture返回，profile登录接口的入参（yaml文件）
	:return: 拼接后的cookie
	'''
	# print(get_param_login)
	cookie = ''
	response = obj_request.get(url=get_param_login['url'], params=get_param_login['data'])  # 调用profile登录接口
	# assert response.json()['status'] == get_param_login['expect']['status']
	if response.json()['status'] == get_param_login['expect']['status']:  # 判断接口响应参数status与预期参数一直，则表示接口调用正常
		set_cookie = response.headers['Set-Cookie']  # 获取响应请求头中的Set-Cookie

		'''截取Set-Cookie中的uuzu_UNICKNAME和uuzu_UAUTH，并拼接'''
		startIndex_UNICKNAME = set_cookie.find('uuzu_UNICKNAME')  # 查询uuzu_UNICKNAME字符串，返回首字符的下标
		endIndex_UNICKNAME = set_cookie.find(' ', startIndex_UNICKNAME)  # 从uuzu_UNICKNAME首字符下标开始查找第一个空格，返回空格的下标
		str_UNICKNAME = set_cookie[startIndex_UNICKNAME:endIndex_UNICKNAME]  # 截取uuzu_UNICKNAME字符串首字符下标到第一个空格下标之间的字符串

		startIndex_UAUTH = set_cookie.find('uuzu_UAUTH')  # 查询uuzu_UAUTH字符串，返回首字符的下标
		endIndex_UAUTH = set_cookie.find(' ', startIndex_UAUTH)  # 从uuzu_UAUTH首字符下标开始查找第一个空格，返回空格的下标
		str_UAUTH = set_cookie[startIndex_UAUTH:endIndex_UAUTH]  # 截取uuzu_UAUTH字符串首字符下标到第一个空格下标之间的字符串
		cookie = str_UNICKNAME + str_UAUTH  # 拼接两个字符串
	# print(cookie)
	return cookie


# 要开放main来调试，需要注释上面@pytest.fixture()，并在函数名称conf_getCookie前面加上test_（如此才能被main函数识别）
# if __name__ == '__main__':
# 	pytest.main(['-v', '-s', 'conftest.py'])
