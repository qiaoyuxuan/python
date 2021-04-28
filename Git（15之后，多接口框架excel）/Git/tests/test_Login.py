#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/16 9:35
author：乔誉萱
说明：获取登陆token
实现单api验证，yaml文件实现参数化
:param OperationYaml 获取yaml文件内容
:param Requests 封装的接口方法
'''
import pytest,json
from Git.utils.operationYaml import OperationYaml
from Git.base.method import Requests


class Test_getLoginToken(object):
	'''将读取到的yaml文件数据，循环放入datas进行参数化，调用登陆接口'''
	@pytest.mark.parametrize('datas',OperationYaml.readYaml_list('data','pro_login.yml'))
	def test_getToken(self,datas):
		obj_request = Requests()
		result = obj_request.post(
			url=datas['url'],
			headers=datas['header']
		)
		expect = datas['expect']['message']
		assert expect in json.dumps(result.json(),ensure_ascii=False)  # 断言:判断yaml文件中的预期结果与接口返回结果是否一致


if __name__ == '__main__':
	pytest.main(['-s','-v','test_Login.py'])
