#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/12 18:24
author：乔誉萱
说明：
:param 
:param 
'''
from unittest import mock

# mock模拟返回值是403，输出后就是403，return_value是固定参数，它是调用mock时返回的值
client = mock.Mock(return_value=403)
print(client())
