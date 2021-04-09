
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from PageLocators.loginpage_locators import LoginPageLocator as loc

class IndexPage:
    def __init__(self,driver):
        self.driver=driver



    def  isExit_logout_ele(self):

        #如果存在就返回True 如果不存在 就返回False
        try:
            time.sleep(2)
            EC.visibility_of_element_located((By.XPATH,'//a[@href="/Index/logout.html"]'))
            return True
        except:
            return False

    #选标操作  默认选第一个 = 元素定位的时候 过滤掉不可以投的标
    def click_first_bid(self,loc):
        elce = self.driver.find.element(*loc.bid)
        elce.click()

    def click_bid_rendom(self,loc):
        #找到所有符合的标
        elce=self.driver.find.elements(*loc.bid)  #找到全部符合的元素
        #随机数生成
        index=random.randint(0,len(elce)-1)
        elce[index].click()





