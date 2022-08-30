from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_usename(self, usename):
        # 调用父类中输入方法
        self.base_input(page.mp_usename, usename)

    """ 
    # 输入密码
    def page_input_passkey(self):
        pass
    """

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类中输入方法
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login(self):
        # 调用父类中点击方法
        sleep(1)
        self.base_click(page.mp_click_btn)

    # 获取昵称--》测试脚本层断言调用
    def page_get_nickname(self):
        # 调用父类中获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务封装-->测试脚本层调用
    def page_mp_login(self, usename, code):
        log.info("正在调用后台管理系统登录业务方法，用户名：{ } 密码：{ }".format(usename, code))
        # 调用page本页面中的操作步骤
        self.page_input_usename(usename)
        self.page_input_code(code)
        self.page_click_login()

    #  组合业务方法-->发布文章依赖使用
    def page_mp_login_success(self, usename="13812345678", code="246810"):
        log.info("正在调用后台管理系统登录业务方法，用户名：{ } 密码：{ }".format(usename, code))
        # 调用page本页面中的操作步骤
        self.page_input_usename(usename)
        self.page_input_code(code)
        self.page_click_login()
