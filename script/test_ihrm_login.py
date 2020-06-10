# 导包
import unittest, requests
from parameterized import parameterized

# 创建测试类
from untils import read_login_data


class TestIHRM(unittest.TestCase):
    # 初始化unittest
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def tearDown(self):
        pass

    # 编写测试函数
    @parameterized.expand(read_login_data())
    def test01_login(self, case_name, request_body, message):
        data = request_body
        response = requests.post(url=self.login_url, json=data)
        # print(response.json())
        #  print('登录接口《{}》测试用例的返回结果：'.format(case_name), response.json())
        # 断言
        self.assertIn(message, response.json().get("message"))
