# 跳转
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:\python\自动化测试\自动化测试day1\练习的html\跳转页面\pop.html")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(10)
driver.quit()

#上传和下拉
# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get(r"E:\python\自动化测试\自动化测试day1\练习的html\上传文件和下拉列表\autotest.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='accountID']").send_keys("wpf")
# driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")
# driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京")
#
# driver.find_element_by_xpath("//*[@id='sexID1']").click()
# driver.find_element_by_xpath("//*[@value='spring']").click()
# driver.find_element_by_xpath("//*[@value='Auterm']").click()
# driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys("E:\python\自动化测试\自动化测试day1\练习的html\上传文件和下拉列表\白冰.jpg")
# time.sleep(9)
# driver.find_element_by_xpath("//*[@id='buttonID']").click()
# driver.quit()
# 弹框
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get(r"E:\python\自动化测试\自动化测试day1\练习的html\弹框的验证\dialogs.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='alert']").click()
# driver.find_element_by_xpath("//*[@id='confirm']").click()
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()



