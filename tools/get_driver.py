from selenium import webdriver


class GetDriver:
    # 1.声明变量
    __web_driver = None

    # 2.获取driver方法封装
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 设置driver操作
            # 1. 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 2. 最大化浏览器
            cls.__web_driver.maximize_window()
            # 3. 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 3.调用关闭driver方法封装
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空driver
            cls.__web_driver = None
