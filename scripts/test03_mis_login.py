import pytest

import page
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMisLogin:
    # 1. 初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2.获取mis对象
        self.mis = page.PageIn(driver).page_get_PageMisLogin()

    # 2.结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3.登录测试业务方法
    @pytest.mark.parametrize("username,pwd,expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, pwd):
        # 1.调用登录业务信息
        self.mis.page_mis_login(username, pwd)
        # 2.断言
        try:
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
            # 1.日志计入
            log.error(e)
            # 2，截图
            self.mis.base_get_img()
            # 3. 抛异常
            raise
