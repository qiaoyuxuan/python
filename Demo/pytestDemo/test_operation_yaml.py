#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/25 20:20
author：乔誉萱
说明：读取yaml文件，使用pytest参数化赋值，验证登陆接口
:param 
:param 
'''
import pytest,requests
import yaml


def readYaml():
	'''读取yaml文件，返回读取内容'''
	with open('../file/pytest_operYaml.yaml',mode='r',encoding='utf-8') as f:
		return list(yaml.safe_load_all(f))


@pytest.mark.parametrize('data',readYaml())
def test_login(data):
	r = requests.post(url=data['url'],headers=data['header'])
	'''yaml中的预期结果和接口实际返回接口对比'''
	assert data['expect']['message'] in r.json()['message']


if __name__ == '__main__':
	pytest.main(['-v','-s','test_operation_yaml.py'])
