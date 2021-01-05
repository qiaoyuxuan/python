#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/3 13:39   乔誉萱
'''

# 百度贴吧url全地址：https://tieba.baidu.com/f?ie=utf-8&kw=%E6%B5%8B%E8%AF%95&fr=search
import requests
'''
url：接口地址
params：get请求，地址?后面的参数
timeout：超时时间，当前接口地址访问若超时，则返回错误
'''
params = {'ie':'utf-8','kw':'自动化测试','fr':'search'}
r = requests.get(url='https://tieba.baidu.com/f',params=params,timeout=1)
print('状态码：',r.status_code)  # 返回状态码
print('响应内容：',r.text) # 服务端返回的任何响应格式，都可以用text获取
# print('json格式：',r.json()) # 仅能用于服务端响应数据格式是json类型的数据，否则会报错，当前即是报错的
print('字节编码：',r.encoding) # 返回响应内容的字节编码
print('响应字节流：',r.content.decode('UTF-8')) # 返回字节流数据，中文需要进行解码utf-8→unicode
