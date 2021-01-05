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
from utils.operationExcel import OperationExcel,ExcelVarles
from common.public import *
from base.method import Requests
import pytest,json


class Test_ApiFlowCase001(object):
	'''实例化类'''
	obj_requests = Requests()  # 接口调用类
	obj_excel = OperationExcel()  # 处理excel文件类
	
	def result(self,row,respons):
		'''断言，接口返回结果与excel中期望结果对比'''
		assert respons.status_code == 200
	
	# assert obj_excel..getExpect(row=row) in json.dumps(respons.json(),ensure_ascii=False)
	
	def test_RunAll(self):
		'''
		1、获取excel中可执行的用例，循环执行
		2、将每个接口的响应参数和用例ID写入yaml文件
		3、每个接口在运行前都用前置参数匹配一下yaml文件，取对出对应的前置参数
		:return:
		'''
		'''清空存放响应参数的yaml文件'''
		OperationYaml.cleanYaml(fileDir='data',fileName='response.yaml')
		get_paramPrev = []
		'''获取可执行的用例，处理参数、并循环执行每条用例'''
		case_list = self.obj_excel.runs()
		for item in case_list:
			url = item[ExcelVarles.caseUrl]  # 获取url
			'''请求头不为空时，则获取请求头'''
			if len(item[ExcelVarles.header.strip()]) > 0:
				header = json.loads(item[ExcelVarles.header.strip()])  # 获取请求头（反序列化和去空格）
			else:
				header = ''
			
			'''请求参数不为空时，则获取请求参数'''
			if len(item[ExcelVarles.params.strip()]) > 0:  # 获取请求参数（反序列化和去空格）
				data = json.loads(item[ExcelVarles.params.strip()])
			else:
				data = ""
			
			'''处理前置参数、执行接口、将响应参数写入yaml文件'''
			if len(item[ExcelVarles.casePre.strip()]) <= 0:
				'''当前置条件为空时，直接执行接口，同时将响应参数和用例ID写入yaml文件'''
				response = self.obj_requests.post(url,headers=header,json=data)  # 执行接口
				res = {}
				res[item[ExcelVarles.caseID]] = response.json()  # 合并用例ID和响应参数
				OperationYaml.writeYaml(fileDir='data',fileName='response.yaml',wType='a',**res)  # 写入yaml文件
			else:
				'''当前置条件不为空时，获取前置条件，去yaml文件中匹配，匹配到后将前置条件更新到请求头和请求参数中，然后执行接口'''
				paramPrev = json.loads(item[ExcelVarles.casePre.strip()])  # 获取前置参数（反序列化和去空格）
				readYaml_dict = OperationYaml.readYaml_dict(fileDir='data',fileName='response.yaml')  # 读取ymal文件
				for k in paramPrev:  # 循环前置参数中的key
					if k in readYaml_dict:  # 如果key与yaml文件中的key匹配到
						'''在yaml文件中查询指定的key，并返回该key和value，用list_to_dict转换dict类型'''
						data = list_to_dict(traverse_take_field(readYaml_dict,paramPrev[k]))
						get_paramPrev.append(data)
				print(get_paramPrev)
				

# if readYaml_dict.get(paramPrev):
# 	print(paramPrev,readYaml_dict)
# else:print('不存在')


# def test_getToken(self):
# 	'''获取登陆token'''
# 	getUrl = self.obj_excel.getUrl(row=1)  # excel中获取url列的第1行，即登陆接口
# 	getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',
# 	                                 row=1)  # excel中获取请求参数列的第1行，返回映射到yaml文件中的详细请求参数
# 	respons = self.obj_requests.post(url=getUrl,
# 	                                 headers=getJson['header'])  # 发送post请求，注意：headers必须指明yaml文件返回数据的['header']部分
# 	# print(r.json()['jwtToken'])
# 	self.result(row=1,respons=respons)  # 断言
# 	writeFile(respons.json()['jwtToken'])  # 将接口返回的jwtToken写入临时文件returnData.txt，供其他接口调用
#
# def test_query(self):
# 	'''查询本公司无着件'''
# 	getUrl = self.obj_excel.getUrl(row=2)  # excel中获取第2行url，即查询无着件接口
# 	getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',
# 	                                 row=2)  # excel中获取请求参数列的第1行，返回映射到yaml文件中的详细请求参数
# 	getJson['header']['token'] = readFile()  # 读取临时文件returnData.txt获取jwtToken，赋予请求头中的token
# 	respons = self.obj_requests.post(url=getUrl,headers=getJson['header'],json=getJson['data'])
# 	self.result(row=2,respons=respons)  # 断言
#
# # print(respons.json())
#
# def test_add(self):
# 	'''上报无着件'''
# 	getUrl = self.obj_excel.getUrl(row=3)
# 	getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',row=3)
# 	getJson['header']['token'] = readFile()
# 	respons = self.obj_requests.post(url=getUrl,headers=getJson['header'],json=getJson['data'])
# 	self.result(row=3,respons=respons)
# 	print(respons.json())
#
# def test_append(self):
# 	'''附加无着件'''
# 	getUrl = self.obj_excel.getUrl(row=4)
# 	getJson = self.obj_excel.getJson(fileDir='config',fileName='apiFlowCase001.yaml',row=4)
# 	getJson['header']['token'] = readFile()
# # respons = self.obj_requests.post(url=getUrl,headers=getJson['header'],json=getJson['data'])
# # self.result(row=4,respons=respons)


if __name__ == '__main__':
	test = Test_ApiFlowCase001()
	test.test_RunAll()
	'''['--alluredir','./report/result']会生成一个json文件，html测试报告会读取该json数据'''
	pytest.main(['-s','-v','test_apiFlowCase001.py::Test_ApiFlowCase001'])
