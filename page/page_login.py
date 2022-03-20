from base.base import Base
import page

from base.get_logger import GetLogger

log = GetLogger().get_logger()
# 通过 包名. 的方式可以获取里面的变量,方法等
class PageLogin(Base):
    # 对元素的操作进行封装
    # 点击登录链接
    def page_click_login_link(self):
        log.info("[page]: 点击链接操作")
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        log.info("[page]: 输入用户名操作")
        self.base_input(page.login_username, username)

    # 输入密码
    def page_input_password(self, password):
        log.info("[page]: 输入密码操作")

        self.base_input(page.login_pwd, password)

    # 输入验证码
    def page_input_verify_code(self, verify_code):
        log.info("[page]: 输入验证码操作")

        self.base_input(page.login_verify_code, verify_code)

    # 点击登录按钮
    def page_click_login_btn(self):
        log.info("[page]: 点击登录按钮")

        self.base_click(page.login_J_login_btn)

    # 获取错误提示信息
    def page_get_error_msg(self):
        log.info("[page]: 获取错误提示信息")

        return self.base_get_text(page.login_err_info)

    # 点击错误提示框确定按钮
    def page_click_error_alert(self):
        log.info("[page]: 点击错误提示框确定按钮")
        self.base_click(page.login_err_ok_btn)

    # 判断是否登录成功(安全退出按钮)
    def page_if_login_success(self):
        # 将元素是否存在的结果返回
        return self.base_element_is_exist(page.login_logout_link)

    # 点击安全退出
    def page_click_logout_link(self):
        log.info("[page]: 点击安全退出")

        self.base_click(page.login_logout_link)

    # 判断是否退出成功
    def page_if_logout_success(self, loc):
        return self.base_element_is_exist(page.login_link)

    # 组合业务方法 -->登录业务直接调用
    def page_login(self, username, password, verify_code):
        log.info("[page]:  正在执行组合业务方法{},{},{}".format(username,password,verify_code))

        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()

# 组合登录业务方法 -->除登录模块的其它模块依赖登录业务直接调用
    def page_login_success(self, username="13800138006", password="123456", verify_code="8888"):
        log.info("[page]:  正在执行组合业务方法{},{},{}".format(username,password,verify_code))

        # 点击登录链接
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_input_verify_code(verify_code)
        self.page_click_login_btn()
