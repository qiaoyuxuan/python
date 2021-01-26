#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/26 13:38
author：乔誉萱
说明：base64 加密和解密
:param 
:param 
'''
import base64

str1='http://www.baidu.com'
result=base64.b64encode(str1.encode('utf-8'))   # 加密
print('加密串：{0}'.format(str(result)))
result=base64.b64decode(result)     # 解密
print('解密串：{0}'.format(result))