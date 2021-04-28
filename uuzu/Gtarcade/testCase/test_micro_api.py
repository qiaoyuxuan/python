#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/27 16:55 
@Author : 乔乔 
@File : test_micro_api.py
:param 
:param 
:param 
'''
from uuzu.Gtarcade.common.method import Requests
from uuzu.Gtarcade.common.get_params import *
from uuzu.Gtarcade.common import *
import pytest, requests

obj_request = Requests()
gameid_list = []  # 全局变量，存放游戏id

# @pytest.mark.skip(reason='忽略执行')
def test_gamelist(conf_getCookie, get_param_gamelist):
	'''
	获取游戏中心游戏列表
	:param conf_getCookie: profile登录接口cookie
	:param get_param_gamelist: 获取的接口参数
	:return:
	'''
	get_param_gamelist['header']['cookie'] = conf_getCookie  # 赋值登录cookie
	res = obj_request.post(url=get_param_gamelist['url'], headers=get_param_gamelist['header'])

	assert res.json()['msg'] == get_param_gamelist['expect']['msg']

	if len(res.json()['data']) > 0:  # 判断如果接口返回data数量>0，就取game_id放入全局变量gameid_list中
		for i in range(len(res.json()['data'])):
			gameid_list.append(res.json()['data'][i]['game_id'])


def test_gamedetails(conf_getCookie, get_allparam_gamelist):
	'''
	新版游戏详情/游戏专区新闻 两个接口
	:param conf_getCookie: profile登录接口cookie
	:param get_allparam_gamelist: 获取的接口参数
	:return:
	'''
	get_allparam_gamelist['header']['cookie'] = conf_getCookie # 赋值登录cookie
	for i in range(len(gameid_list)): # 遍历游戏ID
		get_allparam_gamelist['data']['game_id'] = gameid_list[i] # 赋值游戏ID
		res = obj_request.get(url=get_allparam_gamelist['url'],
		                       headers=get_allparam_gamelist['header'],
		                       params=get_allparam_gamelist['data'])
		print('遍历游戏ID：',gameid_list[i])
		assert res.json()['msg']==get_allparam_gamelist['expect']['msg']


if __name__ == '__main__':
	pytest.main(['-v', '-s', 'test_micro_api.py'])
