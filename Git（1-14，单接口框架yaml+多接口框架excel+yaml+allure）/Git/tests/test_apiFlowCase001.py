#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/17 10:13
author：乔誉萱
说明：
1、多接口业务流程测试，读取data下apiFlowCase001.xls设计的接口进行业务流程测试
2、apiFlowCase001.xls中“请求参数”映射到config/apiFlowCase001.yaml文件中，获取详细请求参数
3、登陆接口返回的jwtToken写入临时文件returnData.txt中，给后续接口使用
:param OperationYaml 操作yaml文件
:param OperationExcel 操作excel文件
:param Requests 接口
:param public.*
'''
from utils.operationYaml import OperationYaml
from utils.operationExcel import OperationExcel
from common.public import *
from base.method import Requests
import pytest,json,allure

class Test_ApiFlowCase001(object):
	'''实例化类'''
	obj_requests = Requests()  # 接口调用类
	obj_excel = OperationExcel()  # 处理excel文件类
	obj_yaml = OperationYaml()  # 处理yaml文件类
	
	def result(self,row,respons):
		'''断言，接口返回结果与excel中期望结果对比'''
		assert respons.status_code == 200
		assert self.obj_excel.getExpect(row=row) in json.dumps(respons.json(),ensure_ascii=False)
	
	@allure.title('登陆')
	@allure.epic('获取登陆token，作为其他接口的请求头')
	def test_getToken(self):
		'''获取登陆token'''
		getUrl = self.obj_excel.getUrl(row=1)  # excel中获取url列的第1行，即登陆接口
		getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',
		                                 row=1)  # excel中获取请求参数列的第1行，返回映射到yaml文件中的详细请求参数
		respons = self.obj_requests.post(url=getUrl,
		                                 headers=getJson['header'])  # 发送post请求，注意：headers必须指明yaml文件返回数据的['header']部分
		# print(r.json()['jwtToken'])
		self.result(row=1,respons=respons)  # 断言
		writeFile(respons.json()['jwtToken'])  # 将接口返回的jwtToken写入临时文件returnData.txt，供其他接口调用
	
	@allure.title('查询本公司无着件')
	@allure.epic('查询当前登陆用户所属公司全部无着件')
	def test_query(self):
		'''查询本公司无着件'''
		getUrl = self.obj_excel.getUrl(row=2)  # excel中获取第2行url，即查询无着件接口
		getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',
		                                 row=2)  # excel中获取请求参数列的第1行，返回映射到yaml文件中的详细请求参数
		getJson['header']['token'] = readFile()  # 读取临时文件returnData.txt获取jwtToken，赋予请求头中的token
		respons = self.obj_requests.post(url=getUrl,headers=getJson['header'],json=getJson['data'])
		self.result(row=2,respons=respons)  # 断言
	
	# print(respons.json())
	
	@allure.title('无着件上报')
	def test_add(self):
		'''上报无着件'''
		getUrl = self.obj_excel.getUrl(row=3)
		getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',row=3)
		getJson['header']['token'] = readFile()
		respons = self.obj_requests.post(url=getUrl,headers=getJson['header'],json=getJson['data'])
		self.result(row=3,respons=respons)
		print(respons.json())
	
	@allure.title('附加上报无着件')
	def test_append(self):
		'''附加无着件'''
		getUrl = self.obj_excel.getUrl(row=4)
		getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',row=4)
		getJson['header']['token'] = readFile()


# respons = self.obj_requests.post(url=getUrl,headers=getJson['header'],json=getJson['data'])
# self.result(row=4,respons=respons)


if __name__ == '__main__':
	test1 = Test_ApiFlowCase001()
	test1.test_getToken()
	
	'''执行用例，并在/report/result路径下生成json文件，后续测试报告html会读取该json'''
	pytest.main(['-s','-v','test_apiFlowCase001.py::Test_ApiFlowCase001','--alluredir','./report/result'])
	import subprocess
	
	'''在report目录下生成一个html，如果已生成将原来的清空'''
	subprocess.call('allure generate report/result/ -o report/html --clean',shell=True,)
	'''生成本地服务，用于展示html测试报告（注意：端口不能被占用）'''
	subprocess.call('allure open -h 127.0.0.1 -p 8088 ./report/html',shell=True)
