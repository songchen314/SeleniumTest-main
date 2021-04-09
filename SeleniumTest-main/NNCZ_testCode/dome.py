



from selenium import webdriver
import time
#selenium
driver=webdriver.Chrome()
driver.get("https://cms2.nncz.cn/login")
driver.find_element_by_xpath('//input[@name="phone"]').send_keys("15388030234")
driver.find_element_by_xpath('//input[@name="password"]').send_keys("123666")
driver.find_element_by_xpath('//button[@class="btn btn-lg btn-login btn-block"]').click()
driver.get("https://cms2.nncz.cn/wechat-bind")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/input').send_keys("15388030234")
time.sleep(3)
driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/ul/li').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/input').send_keys("18601752135")
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/button/span').click()
time.sleep(10)
driver.quit()
