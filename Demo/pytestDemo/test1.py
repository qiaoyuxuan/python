#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/7 19:52
author：乔誉萱
说明：
:param 
:param 
'''
# import json,os,yaml,pytest,requests
#
#
# def getPath():
# 	path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'file/pytest_operYaml.yaml')
# 	return path
#
#
# def read_yaml():
# 	with open(file=getPath(),mode='r',encoding='utf-8') as f:
# 		return list(yaml.safe_load_all(f))
#
#
# @pytest.fixture(params=read_yaml())
# def getdata(request):
# 	return request.param
#
#
# def test_getToken(getdata):
# 	r = requests.post(url=getdata['url'],headers=getdata['header'])
# 	print(r.json())
# 	assert getdata['expect']['message'] == r.json()['message']

import json


class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
	
	def student2dict(std):
		return {
			'name':std.name,
			'age':std.age,
			'score':std.score
		}


s = Student('Bob',20,88)
print(json.dumps(s,default=student2dict))
