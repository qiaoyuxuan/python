#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/26 9:26
author：乔誉萱
说明：读取csv文件，使用pytest参数化赋值，验证登陆接口
:param 
:param 
'''
import csv,requests,pytest,json,os
def getPath(dir_name):
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),dir_name)

# print(getPath('file/pytest_operCsv.csv'))

def readCsv():
	'''读取csv文件，返回读取内容需添加到list中，再返回list'''
	data_list = []
	with open(file=getPath('file/pytest_operCsv.csv'),mode='r') as f:
		reader = csv.reader(f)
		next(reader)
		for item in reader:
			data_list.append(item)
	return data_list


@pytest.mark.parametrize('data',readCsv())
def test_login(data):
	'''请求头是字典类型，需要转为字典'''
	r = requests.post(url=data[0],headers=json.loads(data[1]))
	'''csv中的预期结果和接口实际返回接口对比'''
	assert data[2] in r.json()['message']


if __name__ == '__main__':
	pytest.main(['-s','-v','test_operation_csv.py'])
