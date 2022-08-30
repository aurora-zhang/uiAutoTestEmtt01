# 采用UnitTest框架/pytest框架
import pytest

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class Test01MpLogin:
    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2. 通过统一入口获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()
    # 结束函数

    def teardown_class(self):
        # 1.调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parameterizad("usename,code,expert", read_yaml("mp_login.yaml") )
    def test_mp_login(self, usename, code, expect):
        # 1.调用登录业务方法
        self.mp.page_mp_login(usename, code)
        try:
            # 2.断言
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
        # 输出错误信息

            log.error("断言出错，错误信息：{}".format(e))
            # 截图
            self.mp.base_get_img()
            #  抛异常
            raise





