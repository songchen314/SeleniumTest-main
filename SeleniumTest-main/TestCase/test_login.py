import unittest
from selenium import webdriver
from PageObject.login_page import Login_page
from PageObject.index_page import IndexPage
from TestDatas import common_Datas as CD
from TestDatas import login_datas as LD
import ddt
import logging
from util.logs.logg import Mylogger

my_logger = Mylogger()
import pytest


@pytest.mark.usefixtures("session_dome")
@pytest.mark.usefixtures("class_dome")
@pytest.mark.usefixtures("fuction_dome")
@pytest.mark.dome
def test_dome():
    my_logger.info("cehsi1shuju1")
    print("11111111")
    assert False


# 使用access_web,作用域是类级别，类上只执行一次
@pytest.mark.usefixtures("access_web")
# 使用refresh_page,作用域是函数级别，作用在每一个函数上
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    # @classmethod
    # def setUpClass(cls): #每一个测试类运行的方法 首先执行类再执行方法
    #     #通过excel读取本功能当中需要的所有测试数据
    #     #执行顺序:setupclass---->test1--->test2--->test3---->testN--->tearDownclass
    #     my_logger.info("=================所有测试用例之前的,setUpClass整个测试类只执行一次==============")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(CD.web_login_url)
    #     cls.lg = Login_page(cls.driver)  # 尽然每一个方法都要进行实例化，就直接在开始运行的时候进行实例化
    # @classmethod
    # def tearDownClass(cls):
    #     my_logger.info("=================所有测试用例之后的,tearDownClass整个测试类只执行一次==============")
    #
    #     cls.driver.quit()
    #
    # def tearDown(self) -> None:
    #
    #     self.driver.refresh()
    @pytest.mark.parametrize("data", LD.phone_data)
    # #异常用例 手机号格式不正确(大于11位,小于11位,为空,不在号码段)  ddt
    def test_1_login_wrongForam(self, data, access_web):
        access_web[1].login(data["user"], data["password"])

        # 前置 访问页面
        # 步骤 输入用户名 密码 点击登录
        # 断言 登录页面   提示 请输入正确的手机号
        try:
            assert access_web[1].get_erron_from_loginArea() == data["check"]
        except AssertionError:
            logging.exception("断言失败！！！！")
            raise

    @pytest.mark.parametrize("casedata", LD.password_data)
    def test_2_login_wrongPassword_noReg(self, casedata, access_web):
        access_web[1].login(casedata["user"], casedata["password"])
        # 前置 访问页面
        # 步骤 输入用户名 密码 点击登录
        # 断言 登录页面   提示 请输入正确的手机号
        try:
            assert access_web[1].get_errorMag_from_pageCenter() == casedata["check"]
        except AssertionError:
            logging.exception("断言失败！！！！")
            raise

        # 正常用例 登录成功

    # # 正常用例--登录成功
    @pytest.mark.somke
    def test_login_3_success(self, access_web):
        '''
        :param access_web:
        使用access_web函数名称来接收conftest中access_web函数的返回值，
        返回值为元组形式yield (driver,lg)，使用返回值直接用函数名和下表
        eg：access_web[0],access_web[1],如果access_web函数中没有返回值，则无需传参
        :return:
        '''
        # 2、步骤
        # 调用login方法
        access_web[1].login(LD.success_data['user'], LD.success_data['password'])
        # 3、断言
        assert IndexPage(access_web[0]).isExit_logout_ele()


if __name__ == '__main__':
    pytest.main()
