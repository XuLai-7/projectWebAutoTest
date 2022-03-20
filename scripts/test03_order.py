import unittest

from base.get_driver import GetDriver
from base.get_logger import GetLogger
from page.page_cart import PageCart
from page.page_login import PageLogin
from page.page_order import PageOrder

log = GetLogger().get_logger()
class TestOrder(unittest.TestCase):

    def setUp(self):
        self.driver = GetDriver().get_driver()
        # 调用登录依赖方法
        PageLogin(self.driver).page_login_success()
        # 回到首页
        # 实例化 PageOrder
        self.order = PageOrder(self.driver)
        self.order.page_click_index()
        # 上面执行订单模块case所需的前置条件代码

    def tearDown(self):
        GetDriver().quit_driver()

    # 新建 订单模块测试方法
    def test_order(self):
        try:
            #         调用下订单业务方法
            self.order.page_order()
            #           断言
            msg = self.order.page_get_submit_result()
            print(msg)
            # self.assertEqual(msg,"订单提交成功，请您尽快付款！")
            #       文本较长,使用 in 来断言
            self.assertIn("提交成功", msg)
        except Exception as e:
            #           截图
            self.order.base_get_screen_shot()
            #   日志
            # 真正捕获业务层的错误信息,业务层的核心代码需要添加日志
            log.error(e)

