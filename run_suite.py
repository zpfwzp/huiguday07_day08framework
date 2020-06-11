import unittest, time, os, HTMLTestRunner_PY3
# 设置系统路径
from script.test_ihrm_login import TestIHRM

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件中去
suite.addTest(unittest.makeSuite(TestIHRM))
# 定义测试报告的目录和报告名称
# report_path = BASE_DIR + "/report/ihrm{}.html".format(time.strftime("%Y%m%d %H%M%S"))
report_path = BASE_DIR + "/report/ihrm.html"

# 生成测试报告
with open(report_path, mode="wb")as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm系统接口测试", description="我们的IHRM的接口测试报告")
    runner.run(suite)
