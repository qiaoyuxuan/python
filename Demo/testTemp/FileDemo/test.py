#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/28 16:42   乔誉萱
'''

# class Cat(object):
# 	def __call__(self, *args, **kwargs):
# 		print("我是__call__方法")
#
# def eat(self):
#       print("%s在吃鱼...." % self.name)
#
# Cat.__call__(eat)

# import time
#
# '''打印时间戳：输出：1603878174'''
# print(int(time.time()))
#
# '''
# 输出：time.struct_time(tm_year=2020, tm_mon=10, tm_mday=28, tm_hour=17, tm_min=42, tm_sec=54, tm_wday=2, tm_yday=302, tm_isdst=0)
# '''
# print(time.localtime())
#
# '''输出：2020-10-28 17:43:55'''
# '''strftime格式化时间格式'''
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
#
# '''延迟2秒'''
# time.sleep(2)

# import os,time
# from ClassDemo.login_class import *
# Login('乔誉萱','123')
# # file.File('file.json','我是write写入的内容').read_file()
#
# if os.path.exists('c:/log'):  # 判断文件是否存在
# 	os.rename('c:/log',"c:/newlog")  # 对文件或目录重命名
# 	print('log文件存在，已更名为newlog')
# else:
# 	os.mkdir('c:/log')  # 创建文件
# 	print('log文件不存在，已创建log文件')
# time.sleep(2)  # 延迟两秒
# if os.path.exists('c:/log'):  # 判断文件是否存在
# 	os.rmdir('c:/log')  # 删除文件夹
# 	print('已删除log文件')
# if os.path.exists('c:/newlog'):
# 	os.rmdir('c:/newlog')  # 删除文件夹
# 	print('已删除newlog文件')
#
# print('当前文件的目录：',os.path.dirname(__file__))
# dirName = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件的上级上级目录
# newDir = os.path.join(dirName,'classDemo/login')  # 拼接目录到classDemo/login
# f = open(newDir,'r',encoding='UTF-8').read()  # 打开login文件并读取
# print(f)

# import json
#
# text = ('qiao',18,'上海','青浦')
# str1 = json.dumps(text,ensure_ascii=False)  # 序列化 dict-->str
# print(str1,type(str1))  # 输出：["qiao", 18, "上海", "青浦"] <class 'str'>
# dict1 = json.loads(str1)  # 反序列化 str-->dict
# print(dict1,type(dict1))  # 输出：['qiao', 18, '上海', '青浦'] <class 'list'>
# try:
# 	print(1/0)
# except Exception as e:
# 	print(e)
# 	print('error')
# else:
# 	print('else')
# finally:
# 	print('finally')

# import unittest
# from UnittestDemo import setup
#
#
# class MyTestCase(unittest.TestCase):
# 	@classmethod
# 	def setUpClass(cls) -> None:
# 		pass
#
# 	@classmethod
# 	def tearDownClass(cls) -> None:
# 		pass
#
# 	'''用例'''
#
# 	def test_001(self):
# 		'''用例1'''
# 		print('test_001')
#
# 	def test_002(self):
# 		'''用例2'''
# 		print('test_002')
#
#
# if __name__ == '__main__':
# 	# suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
# 	# suite.addTest(MyTestCase("test_002"))
# 	# suite.addTest(MyTestCase("test_001"))
# 	m = setup.SetupTestCase()
# 	suite1 = unittest.TestLoader().loadTestsFromModule(m)
# 	unittest.TextTestRunner(verbosity=2).run(suite1)

import unittest


class SetupTestCase(unittest.TestCase):
	def setUp(self):
		print(u'我来处理用例执行前准备工作')
	
	def tearDown(self):
		print(u'我来处理用例执行结束后清理工作')
	
	'''用例'''
	
	def test_001(self):
		'''用例1'''
		print(u'我是setup模块用例1')
	
	def test_002(self):
		'''用例2'''
		print(u'我是setup模块用例2')


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(SetupTestCase('test_002'))
	suite.addTest(SetupTestCase('test_001'))
	unittest.TextTestRunner(verbosity=2).run(suite)
