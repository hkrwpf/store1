from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()

driver.get("http://suning.com")

driver.maximize_window()

driver.find_element_by_xpath('//*[@id="reg-bar-node"]/a[1]').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("18532051370")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("qwertyuiop12")
# h = driver.current_window_handle
# driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="iar1"]').click()

driver.switch_to.alert(driver.find_element_by_xpath('/html/body/div[5]/div[2]'))

ac = ActionChains(driver)
source = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div[3]/img')
# time.sleep(2)
# ac.click_and_hold(source).move_by_offset(52, 0).perform()
# ac.release().perform()
# driver.find_element_by_xpath('//*[@id="submit"]').click()

try:
    for i in range(100, 200):
        ac.click_and_hold(source).move_by_offset(i, 0).perform()
        ac.release()
except Exception:
    print("解决了")
finally:
    driver.find_element_by_xpath('//*[@id="submit"]').click()























