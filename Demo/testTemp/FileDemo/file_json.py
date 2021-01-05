#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/28 13:47   乔誉萱
Demo：使用序列化dump处理写入文件内容、读取文件内容
'''

import json,time


class FileJson(object):
	def __init__(self,filename,content):
		self.filename = filename  # 文件名称
		self.content = content  # 写入内容
	
	'''写入'''
	def write_file(self):
		# 序列化往指定文件中写入内容，注意有中文时需设置编码方式
		fw = open(self.filename,'a',encoding='UTF-8')
		json.dump(self.content,fw,ensure_ascii=False)
		fw.write('\n')
		fw.close()
	
	'''读取'''
	def read_file(self):
		self.write_file()
		# 文件的上下文处理，使用with会自动关闭文件，无需再调用close()
		with open(self.filename,'r',encoding='UTF-8') as fr:  # 打开并读取文件内容
			for item in fr.readlines():  # 遍历文件内容
				print('读取的文件内容：',item)


if __name__ == '__main__':
	t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  # 获取当前时间
	text = {"time":t,"name":"乔","age":18,"city":"上海"}
	f = FileJson('../../file/file.json',text)
	f.read_file()
