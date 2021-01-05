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
	'''将excel列的索引，分别用下面方法获取，方便后面统一使用'''
	caseID = 0  # 用例ID的索引
	dec = 1  # 描述的索引
	url = 2  # 接口地址的索引
	method = 3  # 请求方法的索引
	json = 4  # 请求参数的索引
	expect = 5  # 期望结果的索引
	
	def getCaseID(self):
		'''用例ID'''
		return self.caseID
	
	def getDec(self):
		'''描述'''
		return self.dec
	
	def getUrl(self):
		'''接口地址'''
		return self.url
	
	def getMethod(self):
		'''请求方法'''
		return self.method
	
	def getJson(self):
		'''请求参数，这里只是请求名称，需映射到yaml文件中获取对应请求参数'''
		return self.json
	
	def getExpect(self):
		'''期望结果'''
		return self.expect


class OperationExcel(OperationYaml):
	'''读excel文件内容，获取行、列、和指定单元格数据'''
	
	def getSheet(self):
		'''获取excel的第一个sheet'''
		con = xlrd.open_workbook(filePath('data','apiFlowCase001.xls'),'r')
		return con.sheet_by_index(0)
	
	@property
	def getRows(self):
		'''特性方法，获取excel的总行数'''
		return self.getSheet().nrows
	
	@property
	def getCols(self):
		'''特性方法，获取excel的总列数'''
		return self.getSheet().ncols
	
	def getValue(self,row,col):
		'''获取指定单元格数据'''
		return self.getSheet().cell_value(row,col)
	
	def getCaseID(self,row):
		'''获取指定行数的：用例ID'''
		return self.getValue(row=row,col=ExcelVarles().getCaseID())
	
	def getDec(self,row):
		'''获取指定行数的：描述'''
		return self.getValue(row=row,col=ExcelVarles().getDec())
	
	def getUrl(self,row):
		'''获取指定行数的：接口地址'''
		return self.getValue(row=row,col=ExcelVarles().getUrl())
	
	def getMethod(self,row):
		'''获取指定行数的：请求方法'''
		return self.getValue(row=row,col=ExcelVarles().getMethod())
	
	def getJson(self,fileDir,fileName,row):
		'''获取指定行数的：请求参数。
		该请求参数是获取指定excel中“请求参数”列作为索引，在对应yaml返回的dict中获取对应请求参数'''
		return OperationYaml.readYaml_dict(fileDir,fileName)[
			self.getValue(row=row,col=ExcelVarles().getJson())]
	
	def getExpect(self,row):
		'''获取指定行数的：期望结果'''
		return self.getValue(row=row,col=ExcelVarles().getExpect())
	



if __name__ == '__main__':
	obj = OperationExcel()
	'''调用getJson请求参数列，输入要访问的yaml文件路径和名称、excel的行数，返回映射到yaml文件中的请求参数'''
	print('请求参数：',obj.getJson('config','apiFlowCase001.yaml',4))
	print('接口地址：',obj.getUrl(4)) # 获取接口地址列的第4行
	print('请求方法：',obj.getMethod(4))# 获取请求方法的第4行
