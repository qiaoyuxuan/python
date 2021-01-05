#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/25 15:19
author：乔誉萱
说明：读取json文件，使用pytest参数化赋值，验证登陆接口
:param 
:param 
'''

import pytest,json,requests


def readJson():
	'''读取json文件，并返回'''
	return json.load(open('../file/pytest_operJson.json',mode='r',encoding='utf-8'))


@pytest.mark.parametrize('data',readJson())
def test_001(data):
	'''请求头是字典类型，需要转为字典'''
	r = requests.post(url=data['url'],headers=data['header'])
	message = r.json()['message']
	'''json中的预期结果和接口实际返回接口对比'''
	assert data['message'] in message


if __name__ == '__main__':
	pytest.main(['-s','-v','test_operation_json.py'])
