import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisLogin(WebBase):
    # 1.输出用户名
    def page_input_usename(self, usename):
        self.base_input(page.mis_username, usename)

    # 2.输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.mis_pwd, pwd)

    # 3.利用JS修改登录按钮属性点击登录按钮
    def page_click_login_btn(self):
        # 1. 处理Js语句
        js = "document.getElementById('inp1').disabled=false"
        # 2. 修改属性
        self.driver.excute_script(js)
        # 3.点击
        self.base_click(page.mis_login_btn)

    # 4.获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 组合业务方法
    def page_mis_login(self, username, pwd):
        log.info("正在调用后台管理系统登录业务方法，用户名：{}，密码：{}".format(username, pwd))
        self.page_input_usename(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 后续业务依赖登录操作成功方法
    def page_mis_login_success(self, username="testid", pwd="testpwd123"):
        log.info("正在调用后台管理系统成功登录业务方法，用户名：{}，密码：{}".format(username, pwd))
        self.page_input_usename(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
