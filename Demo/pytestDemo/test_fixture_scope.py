#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Datetime：2020/12/30 17:06
author：乔誉萱
说明：
scope的应用范围，默认是function，范围大小关系为：function < class < module < session
:param function：它的作用范围是每个测试用例运行之前都会运行一次fixture，销毁代码在测试用例运行之后运行；
:param class：当一个class里面所有用例都调用同一个fixture时，那么在该class里所有用例开始前，仅执行一次fixture；
:param module：在当前.py脚本中所有用例开始前，仅执行一次fixture；
:param session：可以跨.py模块调用，但在多个模块的用例开始前，仅执行一次fixture（示例见：conftest.py、test_fixture_scope_session1.py、test_fixture_scope_session2.py）
'''
import pytest

# @pytest.fixture(scope='function')
# @pytest.fixture(scope='class')
@pytest.fixture(scope="module")
def first():
	print("\n获取用户名")
	a = "Hero"
	return a

class TestCase:
	def test_1(self,first):
		print("test_1：%s" % first)
		assert first == "Hero"
	
	def test_2(self,first):
		print("test_2：%s" % first)
		assert first == "Hero"

def test_3(first):
	print("test_3：%s" % first)
	assert first == "Hero"

if __name__ == '__main__':
	pytest.main(['-v','-s','test_fixture_scope.py'])
