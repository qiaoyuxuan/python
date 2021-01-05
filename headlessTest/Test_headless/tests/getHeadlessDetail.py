#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/5 16:47   乔誉萱
说明：
获取无着件详情：在main函数中先调用上报接口，获取上报id，将id传入无着件详情接口获取详细信息
:param token：登陆token
:param h_id：无着件ID
'''
from Test_headless.base import setUrl
from Test_headless.base import testRunMain
from Test_headless.base import timeStamp
from Test_headless.tests import getLoginToken,headlessAdd
import json,logging


class GetHeadlessDetail(object):
	def __init__(self,token,h_id):
		self.token = token
		self.h_id = h_id
	
	
	
	def headless_detail(self):
		'''获取无着件详情'''
		get_url = setUrl.detail_url()
		headers = {"token":self.token,
		           "Content-Type":"application/json;charset=UTF-8",
		           "channel":"WDGJ"}
		data = {"id":self.h_id}
		response = testRunMain.RunMain()
		result_str = response.run_main("post",get_url,headers,data)
		result_dict = json.loads(result_str)  # 反序列化将str转成dict
		print(result_dict)
		return result_dict


if __name__ == "__main__":
	try:
		get_token = getLoginToken.get_token() #获取登陆token
		get_add = headlessAdd.HeadlessAdd(get_token)
		add_result_list = get_add.headless_Add() #调用无着件上报接口
		# print(add_result_list)
		'''循环获取无着件上报id，循环获取无着件详情'''
		for item in add_result_list:
			get_id = item['data']['id']
			get_class_detail = GetHeadlessDetail(get_token,get_id)
			get_class_detail.headless_detail()
	except Exception as e:
		logging.exception(e)