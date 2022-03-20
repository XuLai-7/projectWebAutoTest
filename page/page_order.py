import unittest
from time import sleep

import page
from base.base import Base


class PageOrder(Base):
    # 1.登录
    # 2.回到首页
    def page_click_index(self):
        # sleep(2)
        self.base_index()

    # 3.点击我的购物车
    def page_click_my_cart(self):
        self.base_click(page.order_my_cart)

    # 4. 点击全选
    def page_click_all_select(self):
        # 判断全选按钮是否没选中，没选中，就点击全选
        # 选中True,没选中 False 取反，点击全选
        # 判断 复选框 is_selected() 是否选中，返回布尔值
        if not self.base_find(page.order_all).is_selected():
            self.base_click(page.order_all)

    # 5.点击去结算
    def page_account(self):
        self.base_click(page.order_account)

    # 有个异步加载（收货人当页面元素加载完成3秒左右才会出现）的问题
    # 备用数据 查找收货人(在找到这个元素之前, 显示等待一直找,直到找到) ---》动态 解决收货人加载慢的问题
    def page_find_person(self):
        # self.base_get_text(page.order_person)
        # 调用显示等待,直到这个收货人元素被找到,说明异步加载完成,才会执行之后的提交订单的方法
        self.base_find(page.order_person)

    # 6.提交订单
    def page_click_submit_order(self):
        self.base_click(page.order_submit)

    # 7.获取提交订单的结果
    # 看到获取就 return
    def page_get_submit_result(self):
        return self.base_get_text(page.order_submit_result)

    # 组装业务方法
    def page_order(self):
        self.page_click_my_cart()
        self.page_click_all_select()
        self.page_account()
        #坑:  收件人信息通过 ajax 异步请求加载,会慢3秒左右才会显示
        # 这里停顿5秒,不然没有收件人信息元素
        # (解决方式1) sleep(5)
        # 使用备用数据,来确定元素查找
        self.page_find_person()
        # (解决方式2 推荐)调用显示等待,直到这个收货人元素被找到,说明异步加载完成,才会执行之后的提交订单的方法
        # 使用的是显示等待时长机制实现, 推荐
        self.page_click_submit_order()
