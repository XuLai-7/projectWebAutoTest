# 新建登录测试类,继承 unittest.Testcase
import unittest

from parameterized import parameterized

from base.get_driver import GetDriver
from page.page_login import PageLogin

# from base.base import base_click
from tools.read_txt import read_txt
from base.get_logger import GetLogger

log = GetLogger().get_logger()


def get_data():
    # 逆向,正向
    # return [("13800138003", "123456", "8888", "账号不存在!", False,),
    #         ("13800138006", "123456", "8888", "", True,)]
    # return [("13800138003", "123456", "8888", "账号不存在!", False,)]
    arrs = []
    for data in read_txt("login.txt"):
        # 列表添加元组
        arrs.append(tuple(data.strip().split(",")))
    # 返回列表下标为1之外的所有元素
    return arrs[2:]


class TestLogin(unittest.TestCase):
    driver = None
    login = None

    @classmethod
    def setUpClass(cls):
        try:
            # 实例化并获取driver
            cls.driver = GetDriver().get_driver()
            # 操作都封装在 PageLogin 类中,先实例化
            cls.login = PageLogin(cls.driver)
            # 点击登录链接 (放在这里很重要,无论正向,逆向 先后 都可以走)
            cls.login.page_click_login_link()
        except Exception as e:
            log.error("错误:", e)

    @classmethod
    def tearDownClass(cls):
        # 关闭driver 驱动对象
        GetDriver().quit_driver()

    # 第三个方法,  新建登录测试方法
    @parameterized.expand(get_data())
    def test_login(self, username, pwd, verify_code, expect_result, status):
        try:
            # 调用组合业务方法
            # @parameterized.expand(username,pwd,verify_code)
            self.login.page_login(username, pwd, verify_code)
            # 判断正向:
            # 根据文本文件中的状态字符串判断
            if status == "true":
                #     断言
                # print(self.login.page_if_login_success())
                self.assertTrue(self.login.page_if_login_success())
                #     点击安全退出
                self.login.page_click_logout_link()
                #     点击登录链接
                self.login.page_click_login_link()
            # 判断逆向:
            else:
                #     获取错误信息
                msg = self.login.page_get_error_msg()
                print(msg)
                # 点击弹窗确定按钮
                self.login.page_click_error_alert()
                try:
                    self.assertEqual(msg, expect_result)
                except Exception as e:
                    # 出错的地方,都需要 log.error
                    log.error("错误:", e)
                    self.login.base_get_screen_shot()
        except Exception as e:
            log.error("错误:", e)
            self.login.base_get_screen_shot()

        # 无论正向,逆向 先后 都可以走
