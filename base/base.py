import allure
from selenium.webdriver.support.wait import WebDriverWait
from  tools.get_log import GetLog

log = GetLog.get_logger()

class Base:
    # 初始化
    def __init__(self, driver):
        """解决driver"""
        self.driver = driver
        log.info = "正在初始化driver"

    # 查找 元素
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认30s
        :param poll: 查找元素频率，默认 0.5s
        :return: 元素
        """
        log.info("正在查找元素：{}".format(loc))
        return (WebDriverWait(self.driver,
                              timeout=timeout,
                              poll_frequency=poll).until(lambda x: x.find_element(*loc)))

    # 输入 方法封装
    def base_input(self, loc, value):
        """

        :param loc: 元素定位信息
        :param value: 输入的值
        :return: 无
        """
        # 1.获取元素
        e1 = self.base_find(loc)
        # 2.清空
        log.info("正在对： {} 元素执行清空操作！".format(loc))
        e1.clear()
        log.info("正在对： {} 元素执行输入{} 操作！".format(loc,value))

        # 3.输入
        e1.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        log.info("正在对： {} 元素执行点击操作！".format(loc))
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 元素文本的值
        """
        log.info("正在对： {} 元素获取文本操作！".format(loc))
        return self.base_find(loc).text
    # 截图
    def base_get_img(self):
        # 1. 调用截图方法
        log.error("正在对错误进行截图！")
        self.driver.get_screenshot_as_file("./image/err.png")
        # 2. 写入报告
        log.error("正在将截图写入报告！")
        self.base_write_img()

    #   将图片写入报告方法(私用）
    def base_write_img(self):
        # 1. 获取图片文件流
        with open("./image/err.png", "rb") as f:
            # 2. 调用allure.attach 附加方法
            allure.attach("错误原因：",f.read(), allure.attach_type.PNG)