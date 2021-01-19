#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/12 18:39
author：乔誉萱
说明：模拟mock，替代client_mock接口的返回值
:param 
:param 
'''
from unittest import mock
from mock.client_mock import *
import unittest


class MockTest(unittest.TestCase):
	def test_success(self):
		success = mock.Mock(return_value=200)
		send_test = success
		self.assertEquals(visit_test(),success())


if __name__ == '__main__':
	unittest.main()
