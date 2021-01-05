#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/16 14:44
author：乔誉萱
说明：读取excel文件,获取行、列、指定单元格数据
基于已设计好的接口用例excel文档，在列数和顺序不变的基础下，封装此类来读取excel数据，实现外部调用对应的列(方法)，输入行数，即可返回单元格数据
1、ExcelVarles类：实现将excel的每一列作为索引，赋值到对应方法中，方便后续直接调用方法名称获取列索引
2、OperationExcel类：
	readExcel方法读取excel文件，getRows获取总行数、getCols获取总列数，getValue获取指定单元格数据
	其他getXXX方法都是调用getValue获取指定列的数据，便于后续调用，
	OperationExcel类继承OperationYaml操作yaml文件的类，用于excel的请求参数映射到yaml文件获取请求参数具体数据
'''
import xlrd
from common.public import filePath
from utils.operationYaml import OperationYaml


class ExcelVarles(object):
	'''将excel表头文字赋予变量，便于后续调用'''
	caseID = '测试用例ID'
	caseModel = '模块'
	caseName = '接口名称'
	caseUrl = '请求地址'
	casePre = '前置参数'
	method = '请求方法'
	paramsType = '请求参数类型'
	params = '请求参数'
	expect = '期望结果'
	isRun = '是否运行'
	header = '请求头'
	status_code = '状态码'


class OperationExcel(OperationYaml):
	'''获取excel的测试数据，并进行相应处理'''
	
	def getSheet(self,fileDir='data',fileName='apiFlowCase002.xls'):
		'''
		获取excel第一个sheet页的所有数据
		:param fileDir: excel所在目录
		:param fileName: excel文件名称
		:return: xlrd.sheet对象
		'''
		con = xlrd.open_workbook(filePath(fileDir=fileDir,fileName=fileName),'r')
		return con.sheet_by_index(0)
	
	def getExcelDatas(self):
		'''
		处理excel数据：表头为key，数据为value，转为dict并循环放入list
		:return: 返回excel所有数据，类型[{},{}]
		'''
		data_list = []
		title = self.getSheet().row_values(0)  # 获取sheet的第1行数据，即表头
		for row in range(1,self.getSheet().nrows):  # 从第2行开始循环
			getValues = self.getSheet().row_values(row)  # 获取每一行的数据
			data_list.append(dict(zip(title,getValues)))  # 将每行与表头zip，并放入list中
		return data_list
	
	def runs(self):
		'''
		获取可执行用例，当[是否执行]列为y时执行，否则不执行
		:return:
		'''
		run_list = []
		for item in self.getExcelDatas():  # 循环excel所有数据
			isRun = item[ExcelVarles.isRun]
			if isRun == 'y':
				run_list.append(item)  # 判断isRun是否为y，是则加入list，否则不加人
			else:
				pass
		return run_list
	
	def responseToYaml(self,caseID,**kwargs):
		'''
		将接口响应参数和接口ID存入yaml文件
		:param caseID：当前接口用例ID
		:param kwargs: 当前接口响应参数
		:return:
		'''
		res = {}
		res[caseID] = kwargs
		obj_Yaml = OperationYaml()
		obj_Yaml.writeYaml('data','response.yaml','a',**res)


if __name__ == '__main__':
	obj = OperationExcel()
	'''调用getJson请求参数列，输入要访问的yaml文件路径和名称、excel的行数，返回映射到yaml文件中的请求参数'''
	# print('请求参数：',obj.getJson('config','apiFlowCase001.yaml',4))
	# print('接口地址：',obj.getUrl(4)) # 获取接口地址列的第4行
	# print('请求方法：',obj.getMethod(4))# 获取请求方法的第4行
	w = {"code":0,"expireTime":"2020-11-19 13:54:32","jwtToken":"kfOWqFRK0","message":"success"}
	obj.responseToYaml('case003',**w)
	print(obj.readYaml_dict('data','response.yaml'))
