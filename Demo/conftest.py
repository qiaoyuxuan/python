#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/1 20:50
author：乔誉萱
说明：
1、fixture装饰器的公用文件，需要被多函数调用的函数可以放在这里，该文件名称必须为conftest.py，是python内定
2、pytest_addoption注册命令行参数，用于不同参数的传递
:param 
:param 
'''
import pytest,pymysql

# conftest.py公用文件，这里被test_fixture_scope_session1.py 和 test_fixture_scope_session2.py调用
@pytest.fixture(scope='session')
def first():
	print("\n获取用户名,scope为class级别只运行一次")
	a = "Hero"
	return a


# conftest.py公用文件，这里被test_fixture_param.py调用了----------------------------------------------------------------
@pytest.fixture()
def connSQL():
	'''使用fixture返回值：数据库连接，返回连接对象'''
	conn = pymysql.connect(host='10.130.10.59',user='tmp',passwd='Yto_69777717',db='yto_headless')
	return conn


@pytest.fixture()
def init_Headless(connSQL):
	'''fixtrue初始化和清理'''
	connSQL  # 初始化：连接数据库
	yield
	connSQL.close()  # 清理：关闭数据库


# 注册命令行参数，这里被test_fixture_addoption.py调用了--------------------------------------------------------------------
def pytest_addoption(parser):
	'''
	注册自定义参数foo到配置对象
	def pytest_addoption(parser)是固定的
	parser.addoption是固定的，参数中action是固定的
	--foo：必须用--，后面的名称可自定义，是配置对象名称
	default：默认值，被调用方（test_fixture_addoption.py）输出
	help：对参数作用的简要说明
	'''
	# dict1 = {'username':'qiao','passwd':'123'}
	parser.addoption('--foo',action='store',default='我是默认值',help='这是案例')
	parser.addoption('--username',action='store',default='我是默认用户名',help='这是案例')
	parser.addoption('--passwd',action='store',default='我是默认密码',help='这是案例')


@pytest.fixture()
def getFoo(request):
	'''
	返回pytest_addoption配置对象中的--foo
	参数request是固定的
	返回值 request.config.getoption 是固定的
	'''
	return request.config.getoption('--foo')


@pytest.fixture()
def getUsername(request):
	'''返回pytest_addoption配置对象中的--username'''
	return request.config.getoption('--username')


@pytest.fixture()
def getPasswd(request):
	'''返回pytest_addoption配置对象中的--passwd'''
	return request.config.getoption('--passwd')
# ----------------------------------------------------------------------------------------------------------------------
