#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/5 13:23   乔誉萱
Demo：使用内置库csv库，读取文件
'''

import csv


class CsvList(object):
	'''读取数据到list，再将list数据写入（追加）'''
	
	def read_csv_list(self):
		'''读取csv文件到list，使用reader()方法返回的是list'''
		getlist = []
		with open('../file/csv_to_list.csv','r') as f:  # with方法操作文件，会自动关闭文件，无需再使用close()
			read = csv.reader(f)
			# next(read) # 从第二行开始读取
			for item in read:  # 循环读取文件内容，加入到list中并返回
				getlist.append(item)
		# print(item,type(item))
		print('读取到list的数据：',getlist)
		return getlist
	
	def write_csv_list(self):
		'''list格式写入csv'''
		getlist = self.read_csv_list()  # 调用读取方法，获取list列表，将读取内容再次写入
		with open('../file/csv_to_list.csv','a',newline='') as f:  # newling=''可以使写入的内容不会隔一行
			write = csv.writer(f)
			write.writerow(getlist)


class CsvDict(object):
	'''读取数据到dict，再将dict数据写入（追加）'''
	
	def read_csv_dict(self):
		'''
		1、读取csv文件到dict，使用DectReader()方法，再强制转换成dict类型
		2、读取到dict的内容，key为列名，value为每行内容
		'''
		getlist = []
		with open('../file/csv_to_dict.csv','r') as f:
			read = csv.DictReader(f)
			for item in read:
				item = dict(item)
				getlist.append(item)  # 将dict元素加入list，并返回
				print('读取到dict的数据：',getlist)
		# print(item['name']) # 读取指定列名的value
		return getlist
	
	# @staticmethod
	def write_csv_dict(self):
		'''dict格式写入csv'''
		header = {'name','age','address'}
		getlist = self.read_csv_dict()  # 调用dict读取方法，获取dict列表，将读取内容再次写入
		with open('../file/csv_to_dict.csv','a',newline='',encoding='gbk') as f:  # newling=''可以使写入的内容不会隔一行
			write = csv.DictWriter(f,header)  # 这里的header表头需要与写入内容表头一致，否则会报错
			write.writeheader() # 写入表头
			write.writerows(getlist) # 写入内容


if __name__ == '__main__':
	list_class = CsvList()
	list_class.write_csv_list()
	
	dict_class = CsvDict()
	dict_class.write_csv_dict()
