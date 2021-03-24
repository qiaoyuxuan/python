#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/29 10:32   乔誉萱
'''
import os,sys

'''拼接目录：拼接到与当前目录的上级平级的目录'''
dir_name=os.path.join(os.path.dirname(os.path.dirname(__file__)),'FileDemo')
print('拼接后的目录：',dir_name) # 打印拼接后的目录

'''将父级目录加入环境变量，其下的目录可以直接相互引用'''
sys.path.append(dir_name) # 将目录加入环境变量
for item in sys.path: # 循环打印环境变量，查看是否添加成功
	print(item)


from Demo.FileDemo import file_json
# import file_json
file_json.FileJson('os.txt','我是通过sys放入环境变量后，在LibDemo模块中调用file_json模块的内容').read_file()


