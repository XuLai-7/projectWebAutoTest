from selenium.webdriver.common.by import By

"""以下为项目服务器地址"""
URL = "http://www.tpshop.com/"

"""登录模块涉及元素 配置信息"""

login_link = By.PARTIAL_LINK_TEXT, "登录"
login_username = By.CSS_SELECTOR, "#username"
login_pwd = By.CSS_SELECTOR, "#password"
login_verify_code = By.CSS_SELECTOR, "#verify_code"
login_J_login_btn = By.CSS_SELECTOR, ".J-login-submit"
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
login_err_ok_btn = By.CSS_SELECTOR, ".layui-layer-btn0"
login_logout_link = By.PARTIAL_LINK_TEXT, "安全退出"

"""购物车模块涉及元素 配置信息"""
cart_search = By.CSS_SELECTOR, "#q"
cart_search_btn = By.CSS_SELECTOR, ".ecsc-search-button"
cart_add_info = By.PARTIAL_LINK_TEXT, "加入购物车"
cart_add_cart = By.CSS_SELECTOR, "#join_cart"
cart_frame_name="layui-layer-iframe1"
cart_frame_id = By.CSS_SELECTOR, "#layui-layer-iframe1"
cart_add_result = By.CSS_SELECTOR, ".conect-title>span"
cart_close_btn = By.CSS_SELECTOR, ".layui-layer-close"

"""订单模块涉及元素 配置信息"""
order_my_cart = By.CSS_SELECTOR, ".c-n"
order_all = By.CSS_SELECTOR, ".checkCartAll"
order_account = By.CSS_SELECTOR, ".gwc-qjs"
# 收货人 备用
order_person= By.CSS_SELECTOR, ".consignee>b"
order_submit= By.CSS_SELECTOR, ".Sub-orders"
order_submit_result= By.CSS_SELECTOR, ".erhuh>h3"

"""支付模块涉及元素 配置信息"""
pay_my_order=By.PARTIAL_LINK_TEXT,"我的订单"
pay_my_order_title="我的订单"
pay_now_payment=By.CSS_SELECTOR,".ps_lj"
pay_payment_title="订单支付-开源商城 | B2C商城 | B2B2C商城 | 三级分销 | 免费商城 | 多用户商城 | tpshop｜thinkphp shop｜TPshop 免费开源系统 | 微商城"
# 结合 src 属性定位 到货到付款元素
pay_on_delivery=By.CSS_SELECTOR,"[src='/plugins/payment/cod/logo.jpg']"
pay_confirm_payment= By.CSS_SELECTOR,".button-confirm-payment"
# 获取结果
pay_payment_result= By.CSS_SELECTOR,".erhuh>h3"