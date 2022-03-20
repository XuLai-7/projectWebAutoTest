from time import sleep

import page
from base.base import Base


class PageCart(Base):
    #     打开首页
    def page_open_index(self):
        # 业务问题，暂停两秒，再打开其它页面
        sleep(5)
        self.base_index()

    #     搜索小米手机
    def page_input_search(self, value="小米手机"):
        self.base_input(page.cart_search, value)

    #     点击搜索按钮
    def page_click_search_btn(self):
        self.base_click(page.cart_search_btn)

    #     点击添加购物车（跳转到详情页）
    def page_click_add_cart_info(self):
        self.base_click(page.cart_add_info)

    #     点击添加购物车
    def page_click_add_cart(self):
        self.base_click(page.cart_add_cart)

    #     获取添加结果
    def page_get_text(self):
        # 需要先切换frame 表单 加载较慢，不建议使用
        # self.base_switch_frame(page.cart_frame_name)
        # 推荐以元素 切换 ???
        self.base_switch_frame(self.base_find(page.cart_frame_id))
        return self.base_get_text(page.cart_add_result)

    #   切换frame表单
    #  关闭窗口
    def page_close_window(self):
        # 首先回到默认主目录
        self.base_default_content()
        self.base_click(page.cart_close_btn)

    # 组和业务调用方法
    def add_cart(self):
        self.page_input_search()
        self.page_click_search_btn()
        self.page_click_add_cart_info()
        self.page_click_add_cart()
