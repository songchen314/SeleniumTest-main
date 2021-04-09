##用来获取路劲得值
import os

base_dir=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# test_case_path=os.path.join(path,'test_data.xlsx')
# print(test_case_path)
# path=os.path.realpath(__file__) #绝对路径
#os.path.split  切回上一级 记得加  [0]  切一次加一个[0]


#配置文件路径
testdatas_dir=os.path.join(base_dir,'TestCase')
print(testdatas_dir)

#登录的测试用例文件
testcases_dir=os.path.join(base_dir,'util/TestCases')

print(testcases_dir)

#测试用例输出文件
htmlreport_dir=os.path.join(base_dir,'util/reports/test.html')
print(htmlreport_dir)

#日志的路劲
logs_dir=os.path.join(base_dir,'util/logs/log.txt')
print(logs_dir)

#截图路径
screenshot_dir=os.path.join(base_dir,'util/screenshot')

print(screenshot_dir)
