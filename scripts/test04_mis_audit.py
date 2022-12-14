import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog

log = GetLog.get_logger()

class TestMisAudit:
    # 1.初始化

    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2. 获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3. 调用成功登录方法
        self.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 4. 获取PageMisAudit对象
        self.audit = self.page_in.page_get_PageMisArticle()

    # 2.结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3.审核文章业务测试方法
    def test_mis_audit(self,title=page.title, channal=page.channle):
        # 1.调用
        self.audit.page_mis_article(title, channal)
        # 2.断言
        try:
            assert self.audit.page_assert_audit()
        except Exception as e:
            # 1.日至
            log.error(e)
            # 2.截图
            self.audit.base_get_img()
            # 3. 抛异常
            raise