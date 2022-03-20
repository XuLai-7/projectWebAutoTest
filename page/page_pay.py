import page
from base.base import Base


class PagePay(Base):
    #  1.成功登录
    # 2.回到首页
    # 3.点击我的订单链接
    def page_click_my_order_link(self):
        self.base_click(page.pay_my_order)

    # 4.点击立即支付
    def page_click_now_payment(self):
        #     先切换窗口
        # 几十个窗口,依据页面title来切换,也是随便切
        self.base_switch_to_window(page.pay_my_order_title)
        self.base_click(page.pay_now_payment)

    # 5.点击货到付款
    def page_click_pay_on_delivery(self):
        #     先切换窗口
        self.base_switch_to_window(page.pay_payment_title)
        # 点击货到付款
        self.base_click(page.pay_on_delivery)

    # 6. 点击确认支付方式
    def page_click_payment_mode(self):
        self.base_click(page.pay_confirm_payment)

    # 7.获取支付结果
    # 看到获取,需要 return
    def page_get_payment_result(self):
        return self.base_get_text(page.pay_payment_result)

    # 封装 组合支付业务方法
    def page_pay(self):
        self.page_click_my_order_link()
        self.page_click_now_payment()
        self.page_click_pay_on_delivery()
        self.page_click_payment_mode()