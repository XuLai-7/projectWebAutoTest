import unittest

from base.get_driver import GetDriver
from page.page_login import PageLogin
from page.page_pay import PagePay
from base.get_logger import GetLogger

log = GetLogger().get_logger()


class TestPay(unittest.TestCase):
    def setUp(self):
        # 获取driver
        self.driver = GetDriver().get_driver()
        # 成功登录
        PageLogin(self.driver).page_login_success()
        # PagePay 类实例化
        # driver 给 Base
        self.pay = PagePay(self.driver)
        # 回到首页
        self.pay.base_index()

    def tearDown(self):
        # 关闭driver
        GetDriver().quit_driver()
        pass

    # 新建 支付测试方法
    def test_pay(self):
        try:
            # 调用组合支付方法
            self.pay.page_pay()
            # 断言
            msg = self.pay.page_get_payment_result()
            print("支付结果: ", msg)
            self.assertIn("订单提交成功", msg)
            # 截图
            self.pay.base_get_screen_shot()
        except Exception as e:
            # 日志
            log.error(e)
