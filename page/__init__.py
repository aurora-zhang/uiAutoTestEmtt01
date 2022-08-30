from selenium.webdriver.common.by import By

from tools.read_yaml import read_yaml

"""
    以下数据为自媒体，后台管理url
"""
# 自媒体url
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理url
url_mis = "http://ttmis.research.itcast.cn/#/"
"""
以下为文章配置数据
"""
title = read_yaml("mis_article.yaml")[0][0]
channle = read_yaml("mis_article.yaml")[0][3]

"""
    以下元素为自媒体模块配置数据信息
"""
# 用户名
mp_usename = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")

# 密码

# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_click_btn = (By.CSS_SELECTOR, ".e1--button--primary")
# 昵称
mp_nickname = (By.CSS_SELECTOR, ".user-name")
# 内容管理
mp_content_manage = By.XPATH, "//span[text()='内容管理']/.."
# 发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章title
mp_title = By.CSS_SELECTOR, "[placeholder = '文章名称']"
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容 定位到body
mp_content = By.CSS_SELECTOR, "#tinymce"
# 文章封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 发表
mp_submit = By.XPATH, "//*[text()='发表']/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章发布成功')]"

"""
 以下配置信息为mis
"""
# 用户名
mis_username = By.CSS_SELECTOR, "[name = 'username']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[name = 'password']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, "#inp1"
# 获取昵称
mis_nickname = By.CSS_SELECTOR, ".user_info"

# 信息管理
mis_info_manage = By.XPATH, "//*[text() ='信息管理']/."
# 内容审核
mis_content_audit = By.XPATH, "//*[text() ='内容审核']/."
# 输入标题
mis_article_title =By.CSS_SELECTOR, "[placeholder ='请输入：文章名称']"
# 输入频道
mis_channal = By.CSS_SELECTOR, "[placeholder ='请输入：文章频道']"
# 查询按钮
mis_find_btn = By.CSS_SELECTOR, ".find"
# 文章ID
mis_id = By.CSS_SELECTOR, ".cell>span"
# 通过按钮
mis_pass_btn = By.XPATH, "//*[text() ='通过']/.."
# 确定按钮
mis_confirm_btn = By.CSS_SELECTOR, ".el_button--primary"
