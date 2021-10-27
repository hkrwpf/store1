from urllib import request
from selenium import webdriver
from cv2 import cv2
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.jd.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="ttbar-login"]/a[1]').click()
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("15130249272")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("qwertyuiop12")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()



ac = ActionChains(driver)
source = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
time.sleep(2)
ac.click_and_hold(source).move_by_offset(100, 0).perform()
ac.release().perform()
time.sleep(3)

# def findPic(target="img1.jpg", template="img2.png"):
#
#     target_rgb = cv2.imread(target)
#
#     target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
#
#     template_rgb = cv2.imread(template, 0)
#
#     res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
#
#     value = cv2.minMaxLoc(res)
#
#     return value[2][0]
#
#
# while True:
#     try:
#         target = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')
#         template = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
#         src1 = target.get_attribute("src")
#         src2 = template.get_attribute("src")
#         request.urlretrieve(src1,"img1.jpg")
#         request.urlretrieve(src2,"img2.png")
#         x = findPic()
#         offset_x,offset_y = 1221,608
#         pyautogui.moveTo(offset_x,offset_y,duration=0.1 + random.uniform(0,0.1 + random.randint(1,100) / 100))
#         pyautogui.mouseDown()
#         offset_y += random.randint(9,19)
#         pyautogui.moveTo(offset_x + int(x * random.randint(15,25) / 20),offset_y,duration=0.18)
#         offset_y += random.randint(-9,0)
#         pyautogui.moveTo(offset_x + int(x * random.randint(19,23) / 20),offset_y,
#                          duration=random.randint(20,31) / 100)
#         offset_y += random.randint(0,8)
#         pyautogui.moveTo(offset_x + int(x * random.randint(19,21) / 20),offset_y,
#                          duration=random.randint(20,40) / 100)
#         offset_y += random.randint(-3,3)
#         pyautogui.moveTo(x + offset_x + random.randint(-3,3),offset_y,duration=0.5 + random.randint(-10,10) / 100)
#         offset_y += random.randint(-2,2)
#         pyautogui.moveTo(x + offset_x + random.randint(-2,2),offset_y,duration=0.5 + random.randint(-3,3) / 100)
#         pyautogui.mouseUp()
#         time.sleep(2)
#         result = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]').text
#         if '不匹配' in result:
#             print("账户名密码不匹配!", result)
#             break
#     except:
#         print("异常!")
#         break














# while True:
#     big_ele = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[1]/img')
#     small_ele = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[2]/div[2]/img')
#     big_src = big_ele.get_attribute('src')
#     small_src = small_ele.get_attribute('src')
#     print(big_src)
#     print(small_src)
#     big_con = request.urlretrieve(big_src,'./imgs/big.jpg')
#     small_con = request.urlretrieve(small_src,'./imgs/small.png')
#
#     # file = open('./imgs/big.png', mode='wb')
#     # file.close()
#     #
#     # file = open('./imgs/small.png', mode='wb')
#     # file.close()
#
#     big_rgb = cv2.imread('./imgs/big.jpg')
#     big_gray = cv2.cvtColor(big_rgb, cv2.COLOR_BGR2GRAY)
#     small_rgb = cv2.imread('./imgs/small.png', 0)
#     res = cv2.matchTemplate(big_gray, small_rgb, cv2.TM_CCOEFF_NORMED)
#     value = cv2.minMaxLoc(res)
#     x = value[2][0]
#     x = x / 340
#
#     action = ActionChains(driver)
#     try:
#         action.click_and_hold(small_ele).move_by_offset(x, 0).perform()
#         action.release().perform()
#         time.sleep(2)
#
#         driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[1]/div[1]/div[2]').click()
#         time.sleep(1)
#     except Exception as e:
#         break
#
# time.sleep(5)
# driver.quit()


























