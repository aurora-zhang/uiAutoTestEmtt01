from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    """
    以下为web项目专属方法

    """
    # 根据显示文本点击指定元素
    def web_base_click_element(self, placeholder_text, click_text):
        # 1. 点击父选框
        loc = By.CSS_SELECTOR, "[placeholder=‘{}’]".format(placeholder_text)
        self.base_click(loc)
        # 2. 暂停
        sleep(1)
        # 3. 点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 判断页面是否包含指定元素
    def web_base_is_exist(self, text):
        # 1. 组装元素配置信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 2. 找元素
        try:
            # 1.找元素，设置查找时间
            self.base_find(loc, timeout=3)
            # 2.匹配结果
            return True
        except:
            return False

