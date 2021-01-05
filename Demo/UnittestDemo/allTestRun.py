#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/11/2 17:14   乔誉萱
'''
import unittest

'''
discover批量执行当前目录下以test_开头的模块
'''

def allTestRun():
	'''放入discover指定要执行的包路径、文件名正则匹配，返回一个suite'''
	suite = unittest.TestLoader().discover(
		start_dir=os.path.dirname(__file__),
		pattern='test_*.py',
		top_level_dir=None)
	return suite


def run():
	unittest.TextTestRunner(verbosity=2).run(allTestRun())


if __name__ == '__main__':
	run()
