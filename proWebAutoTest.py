"""
 自动化测试流程
 1.需求分析
 2.挑选适合做自动化测试的功能
 3.将功能用例转换成自动化测试用例 (新增一列 自动化)
 4.搭建自动化测试环境 (python,selenium,浏览器驱动,  parameterized)
 5.搭建自动化测试项目的框架架构 (PO+uninttest+数据驱动+Log+报告)
    base(基类),page(页面对象),scripts(业务脚本),tool,data(存储测试数据文件),log,images,report
 6.编写代码
 7.执行测试用例
 8.生成测试报告,分析结果.

 B2C: 商家对客户
 B2B: 商家对商家
TPshop: 基于 ThinkPHP MVC 框架
浏览器->后台服务器->数据库服务器
挑选的自动化测试模块: 登录, 购物车(搜索商品添加到购物车), 订单(下订单), 支付  (一整个流程)
登录模块:
13800138006 123456 8888
登录: 正向,逆向
    正向通过,跳转到个人主页
    用户名不能为空!
    密码不能为空!
    验证码不能为空!
    账号不存在!
    账号格式不匹配!
    密码错误!
    验证码错误

数据驱动txt:
    读取封装
转换格式 列表包元组

日志建议标记在操作之前
base,page 模块标记即可
scripts 使用 异常捕获, 打印日志信息,log.error(e)
出错的地方,都需要 log.error, 打印断言错误截图

购物车模块:
base:
    1. 回到首页
    2. 切换 frame 表单方法
    3. 回到默认目录方法
page:
    在page_login.py 中组装一个登录方法作为依赖方法
    打开首页
    搜索小米手机
    点击搜索按钮
    点击添加购物车（跳转到详情页）
    点击添加购物车
    获取添加结果
        切换frame表单
    关闭窗口
        回到默认主目录

    组合业务方法
    unittest 会按照 按照英文字母其次按照数字来排序先后执行 模块文件

订单模块：
    1.登录
    2.回到首页
    3.点击我的购物车
    4.点击全选
        判断全选按钮是否被选中
    5.点击去结算
    6.提交订单
        异步加载（收货人当页面元素加载完成3秒左右才会出现）的问题
    7.获取提交订单的结果
    base: 无新增方法
    page:
    scripts:
        setup 中先完成执行这条订单模块case所需的前置条件代码
        新建订单测试方法
    问题:
        解决 异步加载 获取的信息导致的延迟问题
            #坑:  收件人信息通过 ajax 异步请求加载,会慢3秒左右才会显示
            # 这里停顿5秒,不然没有收件人信息元素
         (解决方式1) sleep(5)
            # 使用备用数据,来确定元素查找
            self.page_find_person()
         (解决方式2 推荐)调用显示等待,直到这个收货人元素被找到,说明异步加载完成,才会执行之后的提交订单的方法
         直接定位异步加载的元素信息,直到找到
          使用的是显示等待时长机制实现, 推荐
            self.page_click_submit_order()
 # 真正捕获业务层的错误信息,业务层的核心代码需要添加日志

支付模块
    1.成功登录
    2.回到首页
    3.点击我的订单链接
    4.点击立即支付
        先切换窗口
    5.点击货到付款
        先切换窗口
    6.点击确认支付方式
    7.获取支付结果

base:
   1. 切换窗口方法
        driver.switch_to.window(调用获取 hand 方法(title))
   2. 获取 handles 方法
        获取当前driver所有窗口的handles
            遍历当前所有的handles
            切换到当前handle
                获取并判断当前窗口的title是否等于 title 参数
                    返回当前 handle
page:
    根据title切换窗口
 # 几十个窗口,依据页面title来切换,也是随便切

scripts:
    setUp
        # 获取driver
        #成功登录
        # 回到首页
    tearDown
    支付测试方法

最难: 切换窗口方法
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
批量执行
 使用 unittest.testsuite 批量执行用例
# 导包
import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
# scripts 中主程序执行
# suite = unittest.defaultTestLoader.discover("./")
# suite = unittest.defaultTestLoader.discover("./scripts")
suite = unittest.defaultTestLoader.discover("./")
# 报告生成的目录及文件名称
dir_path = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 获取文件流并调用 run 方法运行
# html 形式要用 "wb" 二进制形式写入
with open(dir_path, "wb", ) as f:
    HTMLTestRunner(stream=f, title="tphop 自动化测试报告", description="python+PO+unittest+selenium+HTMLTestRunner").run(suite)

生成测试报告
使用 HTMLTestRunner 工具类生成 HTML 测试报告
# 报告生成的目录及文件名称
dir_path = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# 获取文件流并调用 run 方法运行
# html 形式要用 "wb" 二进制形式写入
with open(dir_path, "wb", ) as f:
    HTMLTestRunner(stream=f, title="tphop 自动化测试报告", description="python+PO+unittest+selenium+HTMLTestRunner").run(suite)

如果 dirver 不是单例,那么无法批量执行一个项目的case

"""