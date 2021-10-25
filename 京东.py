from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.jd.com")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("oppor15")
driver.find_element_by_xpath("//*[@class='button']").click()

h = driver.current_window_handle
time.sleep(2)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div").click()
all_h = driver.window_handles

for i in all_h:
    if i != h:
        driver.switch_to.window(i)
        print(driver.title)


driver.switch_to.window(all_h[1])


driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[2]/a").click()
driver.find_element_by_xpath("//*[@id='choose-service']/div[2]/div/div[1]/div[1]").click()
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()

driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("15130249272")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("qwertyuiop12")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
