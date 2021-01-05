#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
author:qiao
登陆案例：使用函数实现
'''


def typeUsername():
	'''输入用户名'''
	username = input('please input username:')
	return username


def typePwd():
	'''输入密码'''
	password = input('please input password:')
	return password


def register(username,password):
	'''注册'''
	temp = username + '|' + password
	f = open('login','w',encoding='UTF-8')
	f.write(temp)


def login(username,password):
	'''
	登陆
	:return:username，password
	'''
	f = open('login','r',encoding='UTF-8')
	for line in f:
		# print(line)
		list1 = line.split('|')
		if list1[0] == username and list1[1] == password:
			return username,password
		else:
			return None


def exit():
	'''退出系统'''
	import sys
	sys.exit(1)


def main():
	while True:
		num = int(input('1.注册；2.登陆；3.退出\n'))
		if num == 1:
			username = typeUsername()
			password = typePwd()
			register(username,password)
		elif num == 2:
			username = typeUsername()
			password = typePwd()
			tuple1 = login(username,password)
			if tuple1 is not None:
				print('恭喜，用户 %s 登陆成功！' % (tuple1[0]))
			else:
				print('登陆失败，请重新登陆！')
		elif num == 3:
			exit()
		else:
			input('输入有误，请选择1,2,3 ：')


if __name__ == '__main__':
	main()
