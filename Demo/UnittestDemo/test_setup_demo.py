#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/30 16:17   乔誉萱
'''
import unittest

'''
此文件创建模式为python unittest file，执行顺序根据askii码，使用python file创建文件可以根据addTest添加顺序执行
每执行一个用例，setUp和tearDown都会执行一次
'''


class SetupTestCase(unittest.TestCase):
	def setUp(self):
		print('执行前')
	
	def tearDown(self):
		print('清理---------------------------------------------')
	
	def test_001(self):
		'''assertEqual(),内容一致则通过'''
		message = 'success'
		self.assertEqual(message,'Fail')

	def test_002(self):
		'''assertTrue(),返回True则成功，返回False则失败'''
		isbool = False
		self.assertTrue(isbool,'返回False则失败')

	def test_003(self):
		'''assertFalse(),返回False则成功，返回True则失败'''
		isbool = True
		self.assertFalse(isbool,'返回True则失败')
	
	def test_004(self):
		'''assertnIn():参数1是否存在参数2中，存在则返回成功'''
		dict1 = {"name":"qiao","message":"success"}
		print(type(str(dict1)))
		self.assertIn("message1",str(dict1),msg='message1不存在{0}中'.format(str(dict1)))
	
	# if __name__ == '__main__':
	# 	suite = unittest.TestSuite()
	# 	suite.addTest(SetupTestCase('test_002'))
	# 	suite.addTest(SetupTestCase('test_001'))
	# 	unittest.TextTestRunner(verbosity=2).run(suite)