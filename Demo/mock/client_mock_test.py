#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/12 18:39
author：乔誉萱
说明：模拟mock，替代client_mock接口的返回值
PS:当前代码mock失败，需参照无涯教程再研究研究
:param 
:param 
'''
from unittest import mock
from mock.client_mock import *
import unittest


class MockTest(unittest.TestCase):
	def test_success(self):
		success = mock.Mock(return_value=200)   # 将mock的返回码设置为200
		send_test = success                     # 将send_test的返回值设置为mock的200
		self.assertEqual(visit_test(),success())   # 断言


if __name__ == '__main__':
	unittest.main()
