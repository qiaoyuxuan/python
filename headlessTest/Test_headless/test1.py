#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/10 12:57
author：乔誉萱
说明：
:param 
:param 
'''

import json,time,unittest,requests

list1 = ['name','qiao','age',18,'address','上海']


# dict1 = dict(zip(list1[0::2],list1[1::2]))
# print('list转dict：',dict(dict1))
# print('dict转list：',list(dict1.items()))
# tuple1 = tuple(list1)
# print('list转tuple：',tuple1)
# print('tuple转list：',list(tuple1))
# print('dict转tuple：',tuple(dict1.items()))
class Test1(object):
	def __init__(self,l):
		self.l = l
	
	@staticmethod
	def t1(list1):
		# list1 = [{'name':'qiao','age':18},'address','上海']
		list3 = []
		for i in range(len(list1)):
			if i == 0:
				dicti = dict(list1[i])
				list3.append(dicti.items())
			else:
				list3.append(list1[i])
		print(list3)
	
	@staticmethod
	def t2():
		list2 = [{'name':'qiao','age':18},'address','上海']
		str = json.dumps(list2,ensure_ascii=False)
		print(type(str),str)
		l = json.loads(str)
		print(type(l),l)
	
	@staticmethod
	def time1():
		print((str(time.time()))[0:10])
		print(time.localtime())
		time.sleep(1)
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))





list1 = [{'name':'qiao','age':18},'address','上海']

# Test1.t1(list1)
# Test1.time1()

# class Test123(unittest.testCase):
# 	@classmethod
# 	def setUpClass(cls):
# 		print('setUpClass')
#
# 	@classmethod
# 	def tearDownClass(cls):
# 		print('tearDownClass')
#
# 	def test_1(self):
# 		print('test_1')
#
# 	@unittest.skip('忽略')
# 	def test_2(self):
# 		print('test_2')
#
# 	def test_3(self):
# 		print('test_3')
#
# 	@staticmethod
# 	def suite():
# 		suite = unittest.TestSuite()
# 		suite.addTest(Test123('test_1'))
# 		suite.addTest(Test123('test_2'))
# 		# unittest.TextTestRunner(verbosity=2).run(suite)
#
# 		suite1=unittest.TestLoader().loadTestsFromModule(Test123)
# 		unittest.TextTestRunner(verbosity=2).run(suite1)
#
#
# if __name__ == '__main__':
# 	Test123.suite()

# g = lambda x:x + 1
# print(g(1))

foo = [1,2,3,4,5,6,7,8,9,10]
print(foo[0])
print(foo[-1])
print(foo[2:6])
print(foo[0::2])
print(foo[0:-1])
print(foo[::-1])

# def is_odd(n):
# 	return n % 2 == 1
#
#
# tmplist = filter(is_odd,[1,2,3,4,5,6,7,8,9,10])
# newlist = list(tmplist)
# print(newlist)

