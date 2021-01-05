#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
2020/10/30 15:40   乔誉萱
'''

'''
测试套件执行
suite套件执行
'''

import unittest
from UnittestDemo import test_setupclass_demo,test_setup_demo,test_case_demo

if __name__ == '__main__':
	'''使用addTest添加用例到套件中，执行套件中的用例，按照添加到addTest中的顺序执行'''
	suite = unittest.TestSuite() # 实例化测试套件
	suite.addTest(setupclass_demo.SetupClassTestCase('test_002')) #将用例加入套件
	suite.addTest(setupclass_demo.SetupClassTestCase('test_001'))
	suite.addTest(setupclass_demo.SetupClassTestCase('test_003'))
	suite.addTest(setupclass_demo.SetupClassTestCase('test_004'))
	unittest.TextTestRunner(verbosity=2).run(suite) #执行用例

	'''使用loadTestsFromModule加载模块到套件中，执行该模块下所有用例，按照ask码顺序执行'''
	suite1 = unittest.TestLoader().loadTestsFromModule(setupclass_demo)  # 将模块放入套件
	unittest.TextTestRunner(verbosity=2).run(suite1)  # 执行套件中的所有用例

	'''使用loadTestsFromTestCase加载类到套件中，执行该类下所有用例，按照ask码顺序执行'''
	suite2 = unittest.TestLoader().loadTestsFromTestCase(test_setup_demo.SetupTestCase)  # 将类放入套件
	unittest.TextTestRunner(verbosity=2).run(suite2)  # 执行套件中的所有用例

	'''使用loadTestsFromName加载用例到套件中，执行该用例，按照ask码顺序执行'''
	suite3=unittest.TestLoader().loadTestsFromName('testcase_demo.TestCaseDemo.test_add') # 将用例名称放入套件
	unittest.TextTestRunner(verbosity=2).run(suite3)  # 执行套件中的所有用例

