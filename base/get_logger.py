import logging.handlers
class GetLogger():
    # 获取logger
    logger = None
    # 在最外侧运行
    # filename="./log/tpshop.log"
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            sh =logging.StreamHandler()
            th = logging.handlers.TimedRotatingFileHandler(filename="../log/tpshop.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8"
                                                           )
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(funcName)s:%(lineno)d)]-%(message)s"
            fm = logging.Formatter(fmt)
            sh.setFormatter(fm)
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
#         返回日志器
        return cls.logger
