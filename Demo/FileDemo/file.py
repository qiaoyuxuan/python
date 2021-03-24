#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/28 13:01   乔誉萱
Demo：使用open读取和写入文本文件
'''

import file_json



class File(object):
	def __init__(self,filename,content):
		self.filename = filename  # 文件名称
		self.content = content  # 写入内容
	
	'''写入到指定的文本文件'''
	def write_file(self):
		w = open(self.filename,'w',encoding='UTF-8')  # 创建/打开文件，这里如果不编码，存入文件的中文会显示成乱码
		w.write(self.content)  # 写入内容
		w.close()
	
	'''读取指定的文本文件'''
	def read_file(self):
		self.write_file()  # 调用write_file方法，写入文件内容
		r = open(self.filename,'r',encoding='UTF-8') # 打开文件，读取文件内容
		content = r.read()
		print('读取到的文件内容：',content)
		r.close()

if __name__ == '__main__':
	text = {"name":"乔","age":18,"city":"上海"}
	f = File('../file/file.json',str(text))
	f.read_file()