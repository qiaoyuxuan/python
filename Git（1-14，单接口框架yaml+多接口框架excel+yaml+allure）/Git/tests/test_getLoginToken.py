#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/16 9:35
author：乔誉萱
说明：获取登陆token,单api验证，将用例参数放入yaml文件，通过以下一点点代码即可完成单接口验证
:param OperationYaml 获取yaml文件内容
:param Requests 封装的接口方法
'''
import pytest,json
from utils.operationYaml import OperationYaml
from base.method import Requests


class Test_getLoginToken(object):
	'''将读取到的yaml文件数据，循环放入datas进行参数化，调用登陆接口'''
	@pytest.mark.parametrize('datas',OperationYaml.readYaml_list('data','login.yaml'))
	def test_getToken(self,datas):
		obj_request = Requests()
		result = obj_request.post(url=datas['url'],headers=datas['header'])
		# print(result.json())
		expect = datas['expect']['message']
		# print(expect)
		assert expect in json.dumps(result.json(),ensure_ascii=False)  # 断言:判断yaml文件中的预期结果与接口返回结果是否一致
	

if __name__ == '__main__':
	pytest.main(['-s','-v','test_getLoginToken.py'])
