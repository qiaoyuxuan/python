#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/30 16:17   乔誉萱
'''
import unittest

'''
此文件创建模式为python file，执行顺序根据askii码，使用python file创建文件可以根据addTest添加顺序执行
setUpClass执行后，会执行全部的用例，最后再执行tearDownClass，这里需要用@classmethod修饰符（作用是无需实例化类）
'''
class SetupClassTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print('setUpClass')
	
	@classmethod
	def tearDownClass(cls):
		print('tearDownClass------------------------------------------------------')
	
	'''用例'''
	@unittest.skip('忽略test_001执行')
	def test_001(self):
		'''SetupClassTestCase用例test_001'''
		print('test_001')
	
	@unittest.skipIf(True,'为True时不执行') # 为True时不执行test_002，并输出文本
	def test_002(self):
		'''SetupClassTestCase用例test_002'''
		print('test_002')
		
	@unittest.skipUnless(False,'为False时不执行')  # 为False时不执行test_003，并输出文本
	def test_003(self):
		'''SetupClassTestCase用例test_003'''
		print('test_003')
		
	@unittest.expectedFailure
	def test_004(self):
		'''SetupClassTestCase用例test_004'''
		self.assertEqual(2-3,1)


# if __name__ == '__main__':
# 	suite = unittest.TestSuite()  # 实例化测试套件
# 	suite.addTest(setupclass_demo.SetupClassTestCase('test_002'))  # 将用例加入套件
# 	suite.addTest(setupclass_demo.SetupClassTestCase('test_001'))
# 	suite.addTest(setupclass_demo.SetupClassTestCase('test_003'))
# 	suite.addTest(setupclass_demo.SetupClassTestCase('test_004'))
# 	unittest.TextTestRunner(verbosity=2).run(suite)  # 执行用例
	
