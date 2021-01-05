import unittest
from Test_headless.tests.testUnittest.test_headlessfunc import TestHeadlessFunc, CaseAll
from Test_headless.tests.testUnittest import test_headlessfunc


# 执行指定case
def test_suite():
    suite = unittest.TestSuite()
    tests = [CaseAll("test_add_headless"), CaseAll("test_get_headless_detail"),
             CaseAll("test_get_headless_list")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)  # verbosity表示测试结果的信息复杂度，有0,1,2三个值（2最详细），不写默认1
    runner.run(suite)


# 执行指定目录下全部case（执行顺序根据case名称排序）
# def test_loader():
    # suite = unittest.TestLoader().discover('../')
    # # print(suite.countTestCases())
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # suite_all = unittest.TestLoader.loadTestsFromTestCase(test_headlessfunc)
    # print(suite_all)


test_suite()
# test_loader()
