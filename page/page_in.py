from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin

class PageIn:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)

    # 获取
        # 获取PageMisAudit对象
        def page_get_PageMisAudit(self):
            return PageMisAudit(self.driver)
