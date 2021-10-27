from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("http://www.qcc.com")

driver.maximize_window()

driver.find_element_by_xpath('/html/body/header/div/ul/li[10]/a').click()


time.sleep(1)
driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
driver.find_element_by_xpath('//*[@id="nameNormal"]').send_keys("18532051370")
driver.find_element_by_xpath('//*[@id="pwdNormal"]').send_keys("qwertyuiop12")
driver.find_element_by_xpath('//*[@id="user_login_normal"]/button').click()

data = driver.window_handles
















