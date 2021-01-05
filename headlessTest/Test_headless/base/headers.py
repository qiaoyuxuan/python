# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/6 9:12
author：乔誉萱
说明：封装接口请求头
'''
from Test_headless.base import *
from Test_headless.tests import getLoginToken


def get_headers():
    get_token = getLoginToken.get_token()
    headers = {"token": get_token,
               "Content-Type": "application/json;charset=UTF-8",
               "channel": "WDGJ"}
    return headers
