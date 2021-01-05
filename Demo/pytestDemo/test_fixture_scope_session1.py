#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/30 16:50
author：乔誉萱
说明：scope='session'的应用范围
:param session：可以跨.py模块调用的,即当有多个.py模块的用例在开始执行前，只需调用一次fixture，就可设置scope='session'，并可将fixture写入conftest.py文件中
'''

import pytest

# 这里的first函数，已经写入conftest.py，并指定fixture(scope='session')
def test_1(first):
	"""用例传fixture"""
	print("session1-test_1：%s" % first)
	assert first == "Hero"


def test_2(first):
	"""用例传fixture"""
	print("session1-test_2：%s" % first)
	assert first == "Hero"


if __name__ == '__main__':
	pytest.main(['-v','-s','test_fixture_scope_session1.py','test_fixture_scope_session1.py'])
