#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/6 9:12
author：乔誉萱
说明：读取指定的csv或excel文件，将内容转为dict，再append到list并返回
:param filename： 文件名称
:param 
'''
import csv,os,xlrd


class ReadFile(object):
	def __init__(self,filename):
		self.filename = filename
	
	def get_file_path(self):
		'''获取文件路径'''
		get_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'datas/' + self.filename)
		return get_path
	
	def read_csv(self):
		'''获取csv文件内容，需传入*.csv格式文件'''
		csv_list = []
		with open(self.get_file_path(),'r') as f:
			read = csv.DictReader(f)  # DictReader以dict格式读取
			for i in read:
				i = dict(i)  # 循环读取后，需要转dict格式再放入list中，方便后续处理，否则是str类型
				csv_list.append(i)  # 将每次读取的dict内容加入list中，并返回
		# print('读取到csv文件内容：',csv_list)
		return csv_list
	
	def read_excel(self):
		'''获取excel文件内容，转为dict，并放入list中，注意这里需传入*.xls格式文件'''
		excel_list = []
		work = xlrd.open_workbook('datas/' + self.filename,encoding_override='utf-8')
		sheet = work.sheet_by_index(0)  # 指向第一个sheet页
		nor = sheet.nrows  # 获取行数
		nol = sheet.ncols  # 获取列数
		for i in range(1,nor):  # 循环行，从索引1，即第2行开始
			get_dict = {}  # 注意：dict声明一定要放在for循环中，否则追加到list中的dict会覆盖，具体原因钉钉有记录
			for j in range(nol):  # 循环列，从索引0开始
				key = sheet.cell_value(0,j)  # 总是取第一行的每一列，循环放入key
				value = sheet.cell_value(i,j)  # 从第2行开始，取每一列循环放入value
				get_dict[key] = value  # 将key和value放入dict中，key为键，value为值
			# print(get_dict)
			excel_list.append(get_dict)  # 没行循环完都将dict放入list中
		# print('读取到excel文件内容：',excel_list)
		return excel_list
	
	def main_read(self):
		'''
		供其他类调用
		判断传入的文件是csv还是xls，然后调用对应的读取方法，并返回读取数据
		'''
		file_type = self.filename.split('.')[1]  # 以.切片返回list，读取索引1，即文件后缀名
		if file_type == 'xls':
			return self.read_excel()  # 调用读取excel文件方法
		elif file_type == 'csv':
			return self.read_csv()  # 调用读取csv文件方法
		else:
			print('请传入*.csv或*.xls后缀的文件！')


if __name__ == '__main__':
	read_obj = ReadFile('headlessAdd.csv')
	print(read_obj.main_read())
