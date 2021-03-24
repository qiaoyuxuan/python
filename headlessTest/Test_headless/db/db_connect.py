# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/6 9:12
author：乔誉萱
说明：数据库连接封装
:param set_sql: sql语句
:param values: sql语句中的传参
:param *args: 数据库连接串(统一封装到common.datas.setDBparam中)
'''
import pymysql,logging
from headlessTest.Test_headless.base import setDBparam


def db_connect(set_sql,values,*args):
	try:
		db = pymysql.connect(*args)
		cursor = db.cursor()
		if values is not None:  # values为sql语句中的参数，判断是否有参数
			cursor.execute(set_sql,values)  # 有则执行sql，传入values
		else:
			cursor.execute(set_sql)  # 无则直接执行sql
		result = cursor.fetchall()  # 返回全部结果
		print(result)
	except Exception as e:
		logging.exception(e)
	finally:
		db.close()
		return result


'''测试代码'''
args = setDBparam.db_headless()
sql = "select count(*) from hp_headless_package  where " \
      "create_time between '2020-09-29' and '2020-09-30' and create_station_code = '210045'"
# values = {"startTime": s_time_stamp, "endTime": e_time_stamp}  # 将sql中要传入的值放入dict
db_connect(sql,None,*args)
