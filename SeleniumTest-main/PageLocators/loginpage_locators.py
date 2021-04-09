
from selenium.webdriver.common.by import By


class LoginPageLocator:  #这个文件只管理文件管理
    name_text = (By.XPATH, "//input[@name='phone']")
    pwd_text = (By.XPATH, "//input[@name='password']")
    login_but = (By.XPATH, "//button[text()='登录']")
    remeber_user = (By.XPATH, "//imput[@name='remember_me]")
    error_from_loginArea=(By.XPATH,"//div[@class='form-error-info']")
    error_from_loginAreaCenter=(By.XPATH,'//div[@class="layui-layer-content"]')
    bid=(By.XPATH,'elce=self.driver.find.elements()')  #//*[text()='抢投标find']

