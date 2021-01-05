#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/5 16:47   乔誉萱
说明：封装接口请求方法，返回接口响应参数，仅支持post和get
:param url：接口地址
:param data：接口参数
:param headers：请求头

'''
import requests,json,logging
from Test_headless.base import setUrl


class RunMain(object):
	def send_post(self,url,headers,data=[]):
		'''post接口，返回接口返回信息，类型是str'''
		return requests.post(url=url,headers=headers,json=data).json()  # 因为这里要封装post方法，所以这里的url和data值不能写死
		# print(result["jwtToken"]) # 可直接获取返回值
		# dumps将dict转换成str：ensure_ascii:支持中文输出；sort_keys:按a到z排序;indent:缩进位。
		# res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
		# print(type(res))
	
	def send_get(self,url,headers,data=[]):
		'''get接口：
		:param url: 接口地址
		:param headers: 请求头
		:param data: 请求参数
		:return: 接口响应结果
		'''
		return requests.get(url=url,json=data,headers=headers).json()
		# res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
		# print(type(res))
		# return res
	
	def run_main(self,method,get_url=None,get_headers=None,data=None):
		result = None
		if method == 'post':
			result = self.send_post(get_url,get_headers,data)
		elif method == 'get':
			result = self.send_get(get_url,get_headers,data)
		else:
			print("testRunMain返回错误：接口类型错误，请传入post或get")
		return result


if __name__ == '__main__':
	'''测试：掉登陆接口'''
	try:
		url = setUrl.token_url()
		headers = {"Content-Type":"application/json;charset=UTF-8",
		           "token":"266d4a5a-bd27-4943-854f-6d63da0ceefe",
		           "channel":"WDGJ"}
		response = RunMain()
		rs = response.run_main("post",url,headers,"")
		print(rs)
	except Exception as e:
		logging.exception(e)
