import unittest
import HTMLTestrunner
from common.dir_config import *
from util.logs.logg import Mylogger
my_logger=Mylogger()
from TestCase.test_login import TestLogin

# from TestHttpRequesttest01 import TestHttptest   #因为他们两的名字是一样的  直接使用 文件名点方法名  不具体到里面的类名  然后下面读取用例从
#loadTestsFromTestCase 改成   loadTestsFromModule

suite=unittest.TestSuite()
# suite.addTest(TestHttptest("test_001"))#测试用例的实例
#执行用例
# runner=unittest.TextTestRunner()

# runner.run(suite)
loader=unittest.TestLoader()
#loader.discover 用于匹配文件下已test开头的测试文件
suite.addTests(loader.discover(testdatas_dir))

#如果测试用例一个一个导入再别人跑你的用例的时候会烦死的
#最优解就是多个用例
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))
with open(htmlreport_dir,"wb")as file:
    runner=HTMLTestrunner.HTMLTestRunner(stream=file, verbosity=2, title=None, description="这个是单元测试报告")
    my_logger.info('开始测试啦!')
    runner.run(suite)

