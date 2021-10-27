from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("http://www.bilibili.com")

driver.maximize_window()

h = driver.current_window_handle

driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div').click()

data = driver.window_handles

driver.switch_to.window(data[1])


driver.find_element_by_xpath('//*[@id="login-username"]').send_keys("15130249272")
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys("qwertyuiop12")
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()








# driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys("鬼畜")
# driver.find_element_by_xpath('//*[@id="nav_searchform"]/div').click()
# driver.switch_to.window(data[2])
# driver.find_element_by_xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]').click()
#
# driver.switch_to.window(data[3])
# driver.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[16]').click()



