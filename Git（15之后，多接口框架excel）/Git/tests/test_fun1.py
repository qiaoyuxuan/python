#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/11/23 10:10
author：乔誉萱
说明：
:param 
:param 
'''
import pytest


def add(a,b):
	return a + b


@pytest.mark.parametrize('a,b,result',[
	pytest.param(1,1,2,id='one'),
	pytest.param(2,2,4,id='two'),
	pytest.param(3,3,6,id='three'),
])
def test_add(a,b,result):
	assert add(a,b)==result


if __name__ == '__main__':
	pytest.main(['-v','-s','test_fun1.py'])
