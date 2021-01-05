# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/6 9:12
author：乔誉萱
说明：封装接口路径
'''

def token_url():
    '''获取网点管家登录token'''
    set_token_url = "http://10.130.10.60:5001/steward/getH5JwtToken"
    return set_token_url


def add_url():
    '''上报无着件接口'''
    set_add_url = "http://10.130.10.60/steward-api/v1/ai/headless/report"
    return set_add_url


def list_url():
    '''查询无着件列表接口'''
    set_list_url = "http://10.130.10.60/steward-api/app/post"
    return set_list_url


def detail_url():
    '''查询无着件详情接口'''
    set_detail_url = "http://10.130.9.50:20003/headlessApp/HeadlessPackageApp/getHeadlessDetailById"
    return set_detail_url
