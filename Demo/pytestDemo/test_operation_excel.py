#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/26 9:48
author：乔誉萱
说明：读取excel文件，使用pytest参数化赋值，验证登陆接口
:param 
:param 
'''
import xlrd,requests,json,pytest


def readExcel():
	'''读取excel文件，返回读取内容需添加到list中，再返回list'''
	data_list = []
	work = xlrd.open_workbook(filename='../file/pytest_operExcel.xls')
	sheet = work.sheet_by_index(0)
	for item in range(1,sheet.nrows):
		data_list.append(sheet.row_values(item))
	return data_list


@pytest.mark.parametrize('data',readExcel())
def test_login(data):
	'''请求头是字典类型，需要转为字典'''
	r = requests.post(url=data[0],headers=json.loads(data[1]))
	'''excel中的预期结果和接口实际返回接口对比'''
	assert data[2] in r.json()['message']


if __name__ == '__main__':
	pytest.main(['-s','-v','test_operation_excel.py'])
