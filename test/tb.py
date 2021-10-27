from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("http://www.taobao.com")

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
driver.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys("15130249272")
driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys("Qwertyuiop12")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()

ac = ActionChains(driver)
ele = driver.find_element_by_xpath('//*[@id="nc_1_n1z"]')
time.sleep(2)
ac.click_and_hold(ele).move_by_offset(300, 0).perform()

ac.release()





data = driver.window_handles


















