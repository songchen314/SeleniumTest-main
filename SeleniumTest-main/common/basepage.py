import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from common import dir_config
from util.logs.logg import Mylogger

my_logger = Mylogger()
# 封装基本函数 - 执行日志，异常处理，失败截图
import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, time=30, poll_frequency=0.5, doc=""):
        """

        :param locator:元素定位类型
        :param time:元素定位方式
        :param poll_frequency:
        :param doc: 块名_页面名称_操作名称_时间
        :return: None
        """
        my_logger.info("等待元素{0}可见".format(locator))
        try:
            # 开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, time, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间点
            end = datetime.datetime.now()
            # 求一个差值，写在日志中，等待了多久
            wait_time = (end - start).seconds
            my_logger.info("{0}:元素{1}亦可见，等待起始时间：{2}，等待结束时间为：{3}，等待时长".format(locator, start, end, wait_time))
        except:
            logging.exception("等待元素可见失败！！！！")
            # 截图
            self.save_srceenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self, locator, doc=""):
        my_logger.info("等待元素出现：{}".format(locator))
        try:
            EC.invisibility_of_element_located(locator)
        except:
            logging.exception("等待元素可见失败！！！！")
            # 截图
            self.save_srceenshot(doc)
            
            raise

    # 查找元素
    def get_element(self, locator, doc=""):
        my_logger.info("查找元素：{}".format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("等待元素可见失败！！！！")
            # 截图
            self.save_srceenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        my_logger.info("{0}点击元素：{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("点击元素失败！！！！")
            # 截图
            self.save_srceenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):

        # 找元素
        # 元素操作输入
        try:
            ele = self.get_element(locator, doc)
            ele.send_keys(text)
        except:
            logging.exception("输入元素失败！！！！")
            # 截图
            self.save_srceenshot(doc)

            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作输入
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！！！！")
            # 截图
            self.save_srceenshot(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作输入
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("获取元素的属性失败！！！！")
            # 截图
            self.save_srceenshot(doc)
            raise

    # alret处理
    def alret_action(self, action="accrpt"):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # j截图
    def save_srceenshot(self, doc=""):
        # 图片名称：名字对应那个用例：模块名_页面名称_操作名称_时间。pm
        file_name = dir_config.screenshot_dir + "/{0}_{1}.png".format(doc,
                                                                      time.strftime("%Y-%m-%H-%M-%S", time.localtime()))
        self.driver.save_screenshot(file_name)
        my_logger.info('截取网页成功，文件路径为：{0}'.format(file_name))
        try:
            self.driver.save_screenshot(file_name)
            my_logger.info("截图成功，图片路径为{}".format(file_name))
            assert (0)
        except:
            logging.exception("截图失败")
            assert (0)
        # start_time=time.time()
        # file_name='{}.png'.format(start_time)
        # file_path=os.path.join(dir_config.screenshot_dir,file_name)
        # self.driver.save_screenshot(file_path,doc=doc)
        # my_logger.info("错误页面截图保存路径为:{}".format(file_path))
