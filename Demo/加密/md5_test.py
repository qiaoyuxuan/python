#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/26 13:28
author：乔誉萱
说明：MD5 加密，解密没找到对应的方法，可能需要用到pycrypto
:param 
:param 
'''
import hashlib


# 加密方式一：
pwd = 'qiao123'
md5 = hashlib.md5()  # 生成MD5对象
md5.update(pwd.encode('utf-8')) # 对数据加密,update点不出来，需要手动输入
pwd = md5.hexdigest()   # 获取密文，hexdigest点不出来，需要手动输入
print(pwd)  # 输出加密后的数据

# 加密方式二：
pwd='qiao123'
pwd=hashlib.md5(bytes(pwd,encoding='utf-8'))    # 对数据加密
print(pwd.hexdigest())      # 获取密文，hexdigest点不出来，需要手动输入