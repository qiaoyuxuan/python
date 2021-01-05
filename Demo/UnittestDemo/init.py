#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/30 16:46   乔誉萱
'''
import unittest

'''这里将测试准备和清理工作分离出来，以便统一管理'''
class Init(unittest.TestCase):
	def setUp(self):
		print('分离出去的setUp');
		
	def tearDown(self):
		print('分离出去的tearDown---------------------------------------------------')