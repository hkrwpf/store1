from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import time
from initpage import InitPage
from Loginoperation import LoginOperation
from selenium import webdriver


@ddt
class TestLogin(TestCase):

    @data(*InitPage.login_success_data)
    def testLoginSuccess(self,testdata):
        username = testdata["username"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]

        driver = webdriver.Chrome()
        loginop = LoginOperation(driver)

        loginop.login(username, pwd)

        result = loginop.getSuccess_result()

        driver.quit()

        self.assertEqual(result, expect)

    # @data(*InitPage.login_error_data)
    # def testLoginError(self, testdata):
    #     username = testdata["username"]
    #     pwd = testdata["pwd"]
    #     expect = testdata["expect"]
    #
    #     driver = webdriver.Chrome()
    #     loginop = LoginOperation(driver)
    #
    #     loginop.login(username, pwd)
    #
    #     result = loginop.getError_result()
    #
    #     driver.quit()
    #
    #     self.assertEqual(result, expect)



















