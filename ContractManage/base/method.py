#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/15 10:19
author：乔誉萱
说明：封装接口调用方法
:param 
:param 
'''

import requests


class Requests(object):
	def request(self,method='',url='',**kwargs):
		'''执行接口'''
		return requests.request(method=method,url=url,**kwargs)
	
	def post(self,url,**kwargs):
		return self.request(method='post',url=url,**kwargs)
	
	def get(self,url,**kwargs):
		return self.request(method='get',url=url,**kwargs)
	
	def put(self,url,**kwargs):
		return self.request(method='put',url=url,**kwargs)
	
	def delete(self,url,**kwargs):
		return self.request(method='delete',url=url,**kwargs)
