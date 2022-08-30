from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    # 文章ID
    article_id = None
    # 1. 点击信息管理
    def page_click_info_manage(self):
        # 1. 强制等待
        sleep(1)
        # 2. 点击
        self.base_click(page.mis_info_manage)
    # 2. 点击内容审核
    def page_click_content_audit(self):
        # 1. 强制等待
        sleep(1)
        # 2. 点击
        self.base_click(page.mis_content_audit)

    # 3. 输入文章标题
    def page_input_article_title(self, title):
        self.base_input(page.mis_article_title, title)

    # 4.输入文章频道
    def page_input_channal(self, channal):
        self.base_input(page.mis_channal, channal)

    # 5.选择待审核状态
    def page_click_status(self, placeholder_text, click_text):
        self.web_base_click_element(placeholder_text, click_text)

    # 6.点击查询按钮
    def page_click_find(self):
        # 1.点击按钮
        self.base_click(page.mis_find_btn)
        # 2.暂停时间
        sleep(2)

    # 7.获取文章ID
    def page_get_article_id(self):
        return self.base_get_text(page.mis_id)

    # 8. 点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 9. 点击确认
    def page_click_confirm_btn(self):
        # 1. 暂停时间 视觉效果
        sleep(1)
        # 2. 点击
        self.base_click(page.mis_confirm_btn)

    # 组合审核文章业务方法
    def page_mis_audit(self, title, channal, placeholder_text, click_text):
        log.info("正在调用审核文章业务操作方法")
        self.page_click_info_manage()
        self.page_click_content_audit()
        self.page_input_article_title(title)
        self.page_input_channal(channal)
        self.page_click_status(placeholder_text, click_text)
        self.page_click_find()
        self.article_id = self.page_get_article_id()
        self.page_click_pass_btn()
        self.page_click_confirm_btn()

    # 4.组装断言业务操作方法
    def page_assert_audit(self):
        log.info("正在调用断言业务操作方法")
        # 1. 暂停3秒
        sleep(3)
        # 2. 选择审核状态
        self.page_click_status(placeholder_text="请选择", click_text ="审核通过")
        # 3.点击查询
        self.page_click_find()
        # 4，等待
        sleep(3)
        # 5. 找寻id,返回结果
        self.web_base_is_exist(self.article_id)

