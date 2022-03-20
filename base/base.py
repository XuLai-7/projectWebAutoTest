import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import page
from base.get_logger import GetLogger

log = GetLogger().get_logger()


class Base:
    # 先自动执行 __init__.py 方法
    def __init__(self, driver):
        # 初始化driver
        log.info("[base]:正在获取初始化 driver 对象:{}".format(driver))
        self.driver = driver
        # self.driver.maximize_window()
        # self.driver.get("http://www.tpshop.com/")

    # 基类,提供公共的方法
    # 查找元素
    def base_find(self, loc, timout=30, poll=0.5):
        log.info("[base]:正在定位元素".format(loc))
        # *loc 解包元组
        # 设置显示等待
        # 所有的元素通过这个查找方法,那所有元素就都设置上了 显示等待, 返回一个元素
        # 改变时长,改变频率

        return WebDriverWait(self.driver, timeout=timout, poll_frequency=poll).until(lambda
                                                                                         x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        log.info("[base]:正在点击元素".format(loc))
        time.sleep(2)
        # print("click run")
        self.base_find(loc).click()

    # 输入元素
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空元素内容
        log.info("[base]:正在清空元素内容".format(loc))
        el.clear()
        # 输入内容
        log.info("[base]:正在输入元素内容".format(loc))
        el.send_keys(value)

    # 获取文本信息
    def base_get_text(self, loc):
        # 获取到之后返回获取到的文本信息
        log.info("[base]:正在获取元素的文本信息".format(loc))
        return self.base_find(loc).text

    # 截图
    def base_get_screen_shot(self):
        # 截图方法是 driver 中的方法
        log.info("[base]:断言出错,正在执行截图")
        self.driver.get_screenshot_as_file("../images/{}.png".format(time.strftime("%Y_%m_%d %H:%M:%S")))

    # 判断元素是否存在 (可用于登录成功或退出的元素判断)
    def base_element_is_exist(self, loc):
        try:
            # 找元素判断,不能等太久
            self.base_find(loc, timout=10)
            # 找到,返回找到,没有找到,报异常,下面这句就不会执行
            log.info("[base]:查找失败".format(loc))
            return True
        except:
            log.info("[base]:查找成功".format(loc))
            return False

    #     购物车模块
    #  1. 回到首页
    def base_index(self):
        # 打开首页网址URL
        time.sleep(2)
        self.driver.get(page.URL)

    #     2. 切换frame 表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    #     3. 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 切换窗口方法
    def base_switch_to_window(self, title):
        log.info("[base]:切换窗口:{}方法".format(title))
        self.base_get_title_handle(title)

    # 获取指定title页面的handle方法
    def base_get_title_handle(self, title):
        # 获取当前页面所有的handles.
        handles = self.driver.window_handles
        for handle in handles:
            log.info("[base]:正在遍历handle:{}方法".format(handle))
            # 切换handle
            log.info("[base]:切换窗口:{}方法".format(handle))
            self.driver.switch_to_window(handle)
            # 获取当前页面title 并判断是否等于 指定参数 title
            if self.driver.title == title:
                log.info("[base]:判断当前页面title是否等于指定的title:{}方法".format(title))
                # 返回当前handle
                log.info("[base]:返回handle:{}方法".format(handle))
                return handle
