#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2021/1/8 11:37
author：乔誉萱
说明：
1、将+排在左边，-排在右边
2、字符串头尾对比，相同的不动，不同的互换位置
:param 
:param 
'''


def func(a,b):
	'''a,b=b,a等价于a=b,b=a'''
	a,b = b,a
	print(a,b)


func(1,2)


def StringSort(list_data):
		'''
		将+排在左边，-排在右边
		思路：
		1、从左边第一个开始检查，如果是‘-’，则与最后一个互换，末尾索引左移 count - 1，接着循环
		2、如果是‘+’，则不作操作，开始索引右移 startindex + 1 ，接着循环
		3、当两边索引重叠或交叉（开头索引 < 末尾索引），结束循环
		'''
		s_index = 0
		count = len(list_data) - 1
		while s_index < count:
			if list_data[s_index] == '-':
				list_data[s_index],list_data[count] = list_data[count],list_data[s_index]
				count -= 1
			else:
				s_index += 1
		return list_data
	
data1 = ['+','+','-','+','-','+','-']
print(StringSort(data1))



def splitStr(list_str):
	'''
	字符串头尾对比，相同的不动，不同的互换位置
	思路：
	1、第一个索引和最后一个索引对比，相同的不动，不同的互换位置
	2、然后第一个索引+1，最后一个索引-1，继续循环对比
	3、当两边索引重叠或交叉（即末尾索引 >= 开头索引），结束循环
	'''
	count = len(list_str) - 1  # 字符串总长度，即末尾索引值
	s_index = 0  # 开头索引值
	while s_index < count:  # 开头索引 < 末尾索引
		if list_str[s_index] != list_str[count]:  # 开头索引和末尾索引对比，如果不相等
			list_str[s_index],list_str[count] = list_str[count],list_str[s_index]  # 则互换
			# print(list_str)
			s_index += 1  # 开头索引+1
			count -= 1  # 末尾索引-1
		else:  # 当两边索引值相等时，不做任何操作，直接移动索引
			s_index += 1
			count -= 1
	return list_str


list1 = [1,2,3,4,2,6,1]
print(splitStr(list1))