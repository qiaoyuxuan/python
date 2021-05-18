#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
'''
@Time : 2021/3/23 14:52 
@Author : 乔乔 
@File : sign.py
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

PS: 登录和注册的sign值生成方法是一样的，只是入参不一样
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
	return string[0:-1]  # 返回到倒数第二位，即去掉最后的&


def get_login_sign(data_sign,mobile):
	'''
	登录接口的sign签名生成方法
	登录yapi：http://yapi.uuzu.com/project/2083/interface/api/44623
	:param mobile:手机类型，传入ios或android
	:return:返回加密后的sign
	'''
	# get_yaml = operationFile.read_Yaml(filedir='testData', filename='sdk_login.yml')  # 读取待加密的数据
	if data_sign['ts'] == '$time':  # 如果ts=$time，则修改待加密数据中ts为当前时间戳，否则就直接取该时间戳
		data_sign['ts'] = int(time.time())
	data_sign['password'] = md5.get_md5(data_sign['password'])  # 密码进行md5加密
	get_key_sort = key_sort(data_sign)  # 调用排序方法，返回根据key首字母排序后的dict
	string = key_join(get_key_sort)  # 调用拼接方法，返回拼接后的字符串

	# 判断手机类型，获取对应的appkey，用作后续加密参数拼接
	appkey = None
	if mobile == 'ios':
		appkey = 'wpRDTS9g7S3usDtzC5t3'
	elif mobile == 'android':
		appkey = 'tMhjPHHzb8q7NGkWvXT8'

	# 拼接字符串和appkey
	string_join_app = string + appkey
	# print('登录sign值拼接后', string_join_app)

	# md5加密拼接好的字符串
	sign_login = md5.get_md5(string_join_app)
	print("登录的sign值:", sign_login)
	return sign_login

# data = get_reg_yaml = operationFile.read_Yaml(filedir='testData', filename='sdk_register.yml')
# # print(data)
# get_login_sign(data['data'], 'android')


def get_reg_sign(data_sign, mobile):
	'''
	排序和拼接注册接口的sign参数
	yapi：http://yapi.uuzu.com/project/2083/interface/api/44616
	:param data_sign：要拼接的字符串，是register_sign.yml文件中data下的字段，由调用的接口传入
	:param mobile:手机类型，传入ios或android
	:return:加密和拼接后的sign参数
	'''
	# print(data_sign)
	data_sign['password'] = md5.get_md5(data_sign['password'])  # 密码进行md5加密

	# 判断手机类型，获取对应的app_id和appkey，用作后续加密参数拼接
	appkey_reg = None
	if mobile == 'ios':
		data_sign['app_id'] = 'DPAjDPqXeswi'
		appkey_reg = 'wpRDTS9g7S3usDtzC5t3'
	elif mobile == 'android':
		data_sign['app_id'] = 'GGus3TVCKHpN'
		appkey_reg = 'tMhjPHHzb8q7NGkWvXT8'

	get_key_sort = key_sort(data_sign)  # 调用排序方法，返回根据key首字母排序后的dict
	string = key_join(get_key_sort)  # 调用拼接方法，返回拼接后的字符串

	# 拼接字符串和appkey
	string_sign = string + appkey_reg

	# md5加密拼接好的字符串
	sign_reg = md5.get_md5(string_sign)
	# print('注册的sign值:', sign_reg)
	return sign_reg


# data = get_reg_yaml = operationFile.read_Yaml(filedir='testData', filename='sdk_register.yml')
# print(data)
# get_sign(data['data'], 'android')


def reg_name(username, range_start, range_end):
	'''
	根据传入的用户名格式，生成新用户名
	:param username: 用户名
	:param range_start：用户名中数字部分的起始数字
	:param range_end：用户名中数字部分的截止数字
	:return: 返回一个list，存放重生成的用户名
	'''
	name_list = []
	for i in range(range_start, range_end):
		name_list.append(username.replace('1', str(i)))  # 替换username中的数字部分，生成多个用户名
	return name_list


# print(reg_name(username='testapp_1@sina.com', range_start=30, range_end=150))
#
