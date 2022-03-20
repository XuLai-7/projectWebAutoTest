from selenium import webdriver

# 获取driver
import page


# 写成类, 使用类变量, 写成单例模式, 获取driver
class GetDriver:
    driver = None

    # 调用两次,会打开两个浏览器
    @classmethod
    def get_driver(cls):
        # 必须要加cls否则后面的程序引用driver报错
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(page.URL)
        return cls.driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 必须置空操作,关闭,地址还在,其它程序再获取会判断为非空,又关闭了,错误.
            cls.driver = None


# if __name__ == '__main__':
#     # 为None 什么也不做,程序的健壮性
#     GetDriver.quit_driver()
