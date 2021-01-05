#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/30 13:21
author：乔誉萱
说明：
1、fixture装饰器初始化与清理结合DB案例
2、数据库连接、关闭被fixture装饰，放入公用的conftest.py中（在根目录）
:param 
:param 
'''
import pymysql,pytest


def test_get_headless(init_Headless,connSQL):
	'''测试用例，调用参数为conftest.py中的fixture
	init_Headless：数据库初始化和关闭
	connSQL：数据库连接对象
	'''
	cursor = connSQL.cursor()
	cursor.execute("select * from hp_headless_package")
	getData = cursor.fetchall()
	for i in getData:
		print(i)

if __name__ == '__main__':
	pytest.main(['-v','-s','test_fixture_sql.py'])