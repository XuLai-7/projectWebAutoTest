# 新建登录测试类,继承 unittest.Testcase
import unittest
from time import sleep

from parameterized import parameterized

from base.get_driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin
from base.get_logger import GetLogger

log = GetLogger().get_logger()

# 购物车模块只执行一次，所以无所谓 class 还是函数
# 用例多次执行 用 class
# 参数化数据用 class
# 没有参数化哪个都一样
class TestCart(unittest.TestCase):
    driver = None
    cart = None

    @classmethod
    def setUpClass(cls):
        try:
            # 实例化并获取driver
            cls.driver = GetDriver().get_driver()
            # 操作都封装在 PageCart 类中,先实例化
            cls.cart = PageCart(cls.driver)
            # 调用成功登录 依赖方法
            PageLogin(cls.driver).page_login_success()

        except Exception as e:
            log.error("错误:", e)

    @classmethod
    def tearDownClass(cls):
        # 关闭driver 驱动对象
        GetDriver().quit_driver()

    # 第三个方法,  新建添加购物车测试方法
    def test_add_cart(self):
        # 跳转到首页
        self.cart.page_open_index()
        # 调用组合添加购物车业务方法
        self.cart.add_cart()
        msg = self.cart.page_get_text()
        # 断言是否添加成功
        self.assertEqual(msg,"添加成功")
        # 关闭窗口
        self.cart.page_close_window()
