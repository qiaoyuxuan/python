#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/13 13:00
author：乔誉萱
说明：封装接口调用方法
'''
import requests

class Requests(object):
	def request(self,method='',url='',**kwargs):
		'''
		判断执行哪个接口，并执行他们
		:param url: 接口地址
		:param method: 请求方法
		:param kwargs: 请求参数
		:return: 接口响应数据
		'''
		if method == 'post':
			return requests.request(method=method,url=url,**kwargs)
		elif method == 'get':
			return requests.request(method=method,url=url,**kwargs)
		elif method == 'put':
			return requests.request(method=method,url=url,**kwargs)
		elif method == 'delete':
			return requests.request(method=method,url=url,**kwargs)
		
	def post(self,url,**kwargs):
		return self.request(method='post',url=url,**kwargs)
	
	def get(self,url,**kwargs):
		return self.request(method='get',url=url,**kwargs)
	
	def put(self,url,**kwargs):
		return self.request(method='put',url=url,**kwargs)
	
	def delete(self,url,**kwargs):
		return self.request(method='delete',url=url,**kwargs)
	

