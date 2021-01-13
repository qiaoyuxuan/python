#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/12 15:10
author：乔誉萱
说明：tmpdir 和 tmpdir_factory--是内置的临时文件操作函数，在测试执行前创建临时文件，测试执行后删除临时文件，用于保存接口之间传递的数据
tmpdir：操作单个，函数级
tmpdir_factory：操作多个，回话级
:param 
:param 
'''
import requests,pytest


@pytest.fixture()
def getToken():
	'''获取无涯老师的书籍系统登录token，需要先启动Book_api下的app.py模块'''
	r = requests.post(
		url='http://127.0.0.1:5000/auth',
		json={'username':'wuya','password':'asd888'})
	return r.json()['access_token']


def test_get_all_books(tmpdir,getToken):
	'''
	使用tmpdir将token写入临时文件，然后读取
	:param tmpdir: tmpdir模块作为函数的参数
	:param getToken:获取token的函数
	:return:
	'''
	print('\n原token：',getToken)
	f = tmpdir.join('token.txt')   # 使用tmpdir创建临时文件token.txt,.join是点不出来的，需要手写
	f.write(getToken)              # 将token写入临时文件,.write是点不出来的，需要手写
	print('读取临时文件',f.read())   # 读取临时数据,.read()是点不出来的，需要手写

if __name__ == '__main__':
	pytest.main(['-v','-s','test_fixture_tmpdir.py'])
