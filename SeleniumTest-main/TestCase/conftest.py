import pytest
from selenium import webdriver
from TestDatas import common_Datas as CD
from PageObject.login_page import Login_page


driver=None
# 声明一个它是一个fixture
# scope='class'表示access_web的作用域在类上，执行测试用例时，类只执行一次
@pytest.fixture(scope='class')
def access_web():
    # 前置条件
    global driver  #声明driver为全局变量
    print("========所有测试用例之前的，整个测试用例只执行一次=========")
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    # 实例化LoginPage类
    lg=Login_page(driver)
    # yield 同时可以返回值(driver,lg)，相当于return，在使用返回值的时候直接用函数名
    yield (driver,lg)  ##前面是前置条件、后面是后置条件
    # 后置条件
    print("========所有测试用例之后的，整个测试用例只执行一次=========")
    driver.quit()
@pytest.fixture()
# @pytest.fixture()表示函数默认作用域access_web的作用域在函数上，执行测试用例时，每个函数都执行一次
def refresh_page():
    global driver
    # 前置操作
    yield
    # 后置操作
    driver.refresh()

@pytest.fixture(scope="session")
def session_dome():
    print("***********我是整个测试会话期间的开始**********")
    yield
    print("***********我是整个测试会话期间的结束**********")


@pytest.fixture(scope="class")
def class_dome():
    print("***********我是class的开始**********")
    yield
    print("***********我是class的结束**********")

@pytest.fixture
def fuction_dome():
    print("***********我是fuction_dome的开始**********")
    yield
    print("***********我是fuction_dome的结束**********")