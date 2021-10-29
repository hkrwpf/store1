from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:8080/HKR")
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("wpf")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
driver.find_element_by_xpath('//*[@id="submit"]').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="img"]').click()
time.sleep(1)
h = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="ul_pic"]/li[8]/img').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="file1"]').send_keys(r"D:\ruanjiandakai\单元测试\day15\picture.jpg")
driver.find_element_by_xpath('//*[@id="pic_btn"]').click()










