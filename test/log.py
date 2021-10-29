from unittest import TestCase
from selenium import webdriver
import time

class TestHkr(TestCase):

    def testLogin(self):
        username = "wpf"
        pwd = "123456"
        expect = "Student Login"


        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        driver.find_element_by_xpath("//*[@id='submit']").click()

        result = driver.title
        driver.quit()
        self.assertEqual(result, expect)

    def testLoginError(self):
        username = "wpf"
        pwd = "1234567"
        expect = "账户名错误或密码错误!别瞎弄!"


        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
        driver.find_element_by_xpath("//*[@id='submit']").click()

        result = driver.find_element_by_xpath("//*[@id='msg_uname']").text
        driver.quit()
        self.assertEqual(result, expect)














