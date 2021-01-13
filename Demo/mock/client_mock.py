#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/12 18:34
author：乔誉萱
说明：这是一段开发程序，
:param 
:param 
'''
import requests

def send_test(url):
	r=requests.get(url=url)
	return r.status_code

def visit_test():
	return send_test('http://127.0.0.1/')

