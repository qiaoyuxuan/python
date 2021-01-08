#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/3 15:23   乔誉萱
Demo：使用xlrd读取excel文件
'''
import os,xlrd


def read_excel(filename):
	'''返回当前路径下指定文件的路径'''
	get_path = os.path.join(os.path.dirname(__file__),'file/data.xls')
	work = xlrd.open_workbook(get_path)  # 打开data.xls文件
	sheet = work.sheet_by_index(0)  # 定位到第一个sheet
	print('总行数：',sheet.nrows)
	print('单元格内容：',sheet.cell_value(3,2)) # 第三行第二列
	print(dir(sheet))
