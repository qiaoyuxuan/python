#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/4/21 15:22 
@Author : 乔乔 
@File : method.py 
:param 
:param 
:param 
'''

import requests


class Requests(object):
	def request(self, method='', url='', **kwargs):
		'''执行接口'''
		return requests.request(method=method, url=url, **kwargs)

	def post(self, url, **kwargs):
		return self.request(method='post', url=url, **kwargs)

	def get(self, url, **kwargs):
		return self.request(method='get', url=url, **kwargs)

	def put(self, url, **kwargs):
		return self.request(method='put', url=url, **kwargs)

	def delete(self, url, **kwargs):
		return self.request(method='delete', url=url, **kwargs)

