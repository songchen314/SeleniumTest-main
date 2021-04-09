from selenium import webdriver
import time
from PageLocators.loginpage_locators import LoginPageLocator as loc
from common.basepage import BasePage


class Login_page(BasePage):


    #登录
    def login(self,user,password,remeber_user=True):
        #输入用户名
        #输入密码
        #点击登录
        doc="登录页面——登录功能"
        time.sleep(2)
        self.driver.implicitly_wait(10)
        self.input_text(loc.name_text,user,doc)
        self.input_text(loc.pwd_text,password,doc)
        self.click_element(loc.login_but,doc)

        # else1=WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(loc.name_text))
        # self.driver.find_element(*loc.name_text).send_keys(username)
        # self.driver.find_element(*loc.pwd_text).send_keys(password)
        #判断一下remeber_user的值，来决定是否勾选
        # self.driver.find_element(*loc.login_but).click()

    #注册
    # def register_enter(self):
    #     WebDriverWait(self.driver,20).until(EC.invisibility_of_element_located((By.XPATH,'')))
    #     self.driver.find_element_by_xpath("").click()

        #1获取错误提示信息,登录区域
    def get_erron_from_loginArea(self):
        time.sleep(2)
        doc="登录页面——登录功能-获取错误提示信息"

        self.wait_elePresence(loc.error_from_loginArea,doc)
        # EC.invisibility_of_element_located((loc.error_from_loginArea))
        return self.get_text(loc.error_from_loginArea,doc)



    #获取错误信息  页面中间的
    def get_errorMag_from_pageCenter(self):
        time.sleep(2)
        doc = "登录页面——登录功能-获取错误信息-页面中间的"
        self.wait_elePresence(loc.error_from_loginAreaCenter,doc)
        # EC.visibility_of_element_located((loc.error_from_loginAreaCenter))
        return self.get_text(loc.error_from_loginAreaCenter,doc)


    #忘记密码
    def register(self):
        pass