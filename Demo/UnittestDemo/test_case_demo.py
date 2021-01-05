#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/30 17:28   乔誉萱
'''
from UnittestDemo.init import *

'''已将setIp和tearDown分离到init模块中，类名Init，这里继承他即可，无需重复写，方便统一管理'''
class TestCaseDemo(Init):
	def test_add(self):
		'''TestCaseDemo用例test_add'''
		print('我是testcase_demo模块的test_add用例')
	
	def test_del(self):
		'''TestCaseDemo用例test_del'''
		print('我是testcase_demo模块的test_del用例')