#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/23 14:52 
@Author : 乔乔 
@File : login_sign.py
****************sign生成方法：***************
Gta账号登录接口：https://sdk.gtarcade.com/sdk/v6/login
登录参数：
app_id: DPAjDPqXeswi
channel_id: 0
device_id: 359B34BF-B83C-43C7-9A37-6DB7F508221A
language: zh_cn
password: e10adc3949ba59abbe56e057f20f883e
ts: 1616411186 (时间戳)
username: vxywang@gmail.common
sign: 加密

sign签名的生成方法：
所有参数的key按照字母顺序排序，得到一个有序字典，
按照顺序拼接：app_id=DPAjDPqXeswi&channel_id=0，以此类推，得到一个很长的字符串,
安卓和ios根据不同的appkey，把appkey拼接在上一步得到的长字符串后面
Android:tMhjPHHzb8q7NGkWvXT8
IOS:wpRDTS9g7S3usDtzC5t3
用MD5运算工具，算出最终的字符串的md5值，就是sign
'''

import time
from uuzu.app.Common import operationFile, md5


def key_sort(body):
	'''
	根据key排序，按首字母从大到小
	:param body: dict数据
	:return: 根据key首字母排序后的dict
	'''
	# print(kwargs.items())
	body_sort = sorted(body.items(), key=lambda x: x[0])  # 排序方法，返回根据key首字母排序后的dict
	# print('排序后：', body_sort)
	return body_sort


def key_join(body):
	'''
	拼接加密字符串
	:param body: 已排好序的待加密字符串
	:return: 拼接后的字符串
	'''
	string = ''
	for i in body:  # 循环list，拼接每个元素并加入一个新的list
		string = string + str(i[0]) + '=' + str(i[1]) + '&'
	return string[0:-1] # 返回到倒数第二位，即去掉最后的&


def login_sign(mobile):
	'''
	sign签名生成方法
	:param mobile:手机类型，传入ios或android
	:return:返回加密后的sign
	'''
	get_yaml = operationFile.read_Yaml('app/testData/login_sign.yaml')  # 读取待加密的数据
	if get_yaml['ts'] == '$time':  # 如果ts=$time，则修改待加密数据中ts为当前时间戳，否则就直接取该时间戳
		get_yaml['ts'] = int(time.time())
	get_yaml['password'] = md5.get_md5(get_yaml['password']) # 密码进行md5加密
	get_key_sort = key_sort(get_yaml)  # 调用排序方法，返回根据key首字母排序后的dict
	string = key_join(get_key_sort)  # 调用拼接方法，返回拼接后的字符串

	# 判断手机类型，获取对应的appkey，用作后续加密参数拼接
	appkey = None
	if mobile == 'ios':
		appkey = 'wpRDTS9g7S3usDtzC5t3'
	elif mobile == 'android':
		appkey = 'tMhjPHHzb8q7NGkWvXT8'

	# 拼接字符串和appkey
	string_join_app = string + appkey
	# print('拼接后', string_join_app)

	# md5加密拼接好的字符串
	sign = md5.get_md5(string_join_app)
	print("sign is:",sign)
	return sign


login_sign('android')
