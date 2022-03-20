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
