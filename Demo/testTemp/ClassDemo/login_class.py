#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/28 10:00   乔誉萱
登陆案例：使用类实现
'''

import json


# 定义个登陆类
class Login(object):
	def __init__(self,username,pwd):  # 构造函数
		self.username = username
		self.pwd = pwd
	
	def get_username(self):
		return self.username
	
	def set_username(self,username):
		self.username = username
	
	def get_pwd(self):
		return self.pwd
	
	def set_pwd(self,pwd):
		self.pwd = pwd
	
	def register(self):
		# 用户名和密码以|相隔，保存到变量中
		temp = self.username + '|' + self.pwd
		# 写入login文件，并将dict转换成json字符串格式
		json.dump(temp,open('login','w',encoding='UTF-8'),ensure_ascii=False)
	
	def login(self,username,pwd):
		# 读取login文件内容，并将json字符串格式转换成dict
		temp = json.load(open('login','r',encoding='UTF-8'))
		list_temp = temp.split('|')
		# 判断登陆账号与保存在login文件中的账号是否一致
		if list_temp[0] == username and list_temp[1] == pwd:
			print('恭喜，用户 {0} 登陆成功！'.format(self.username))
		else:
			print('登陆失败，请重试！')


objLogin = Login('乔誉萱','123')  # 实例化类
objLogin.register()  # 调用注册方法
objLogin.login('乔誉萱','123')  # 调用登陆方法
