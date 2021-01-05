# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/6 9:12
author：乔誉萱
说明：用于在嵌套列表中，查询指定字段的值，返回查询到的值，类型是list；将list转为dict
:param data: 嵌套字典列表
:param fields: 要取出的字段
:param values: 返回的值
:param currentKey: 当前的键值
:return: 列表
'''


def traverse_take_field(data, fields, values=[], current_key=None):
    '''封装方法：查询指定key值是否存在与指定字段'''
    if current_key in fields:  # 当data不是list或dict时，判断当前key是否存在与指定字段
        values.append(current_key)  # key和value放入list中
        values.append(data)
    elif isinstance(data, list):  # 判断data是否为list类型
        for i in data:  # 遍历list
            traverse_take_field(i, fields, values, current_key)  # 将list放入并递归判断list
    elif isinstance(data, dict):  # 判断data是否为dict类型
        for key, value in data.items():  # 遍历dict，使用items()函数
            traverse_take_field(value, fields, values, key)  # 将dict放入并递归判断dict
    return values  # 返回list



def list_to_dict(list_data):
    '''将list转为dict，注意：key不能重复，否则转换出来的dict不对'''
    get_dict = dict(zip(list_data[0::2], list_data[1::2]))
    return get_dict

    # ''' 以下是拆分放入两个list，再合并为一个dict，与上面zip效果一样
    # key, value = [], []
    # i = 0
    # while i < len(data):
    #     if i % 2 == 0:
    #         key.append(data[i])
    #     else:
    #         value.append(data[i])
    #     i += 1
    # print(" key:", key, "\n", "value:", value)
    # get_dict = dict(zip(key, value))
    # print(get_dict)

'''测试'''
dict_test = {'case_001': {'code': 0, 'expireTime': '2020-11-20 19:56:44', 'jwtToken': 'eyJhbG', 'message': 'success'}}
set_fields = ['jwtToken']
result_list = traverse_take_field(dict_test, set_fields)
print(result_list)
result_dict=list_to_dict(result_list)
print(result_dict)

