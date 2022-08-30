import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpArticle:

    # 1. 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2. 获得统一入类对象
        self.page_in = PageIn(driver)
        # 3. 获取pagempLogin对象并成功调用登录依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 4. 获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()



    # 2. 结束函数
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3.测试发布文章业务方法
    @pytest.mark.parametrize("title,content,expect,channel", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect):

        # 1. 调用对象业务方法
        self.article.page_mp_article(title, content )
        # 2. 断言
        try:
            assert expect == self.article.page_get_info()
        except Exception as e:
            log.error("错误信息", e)



