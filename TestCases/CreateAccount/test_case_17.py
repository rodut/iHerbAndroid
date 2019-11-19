import unittest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.CreateAccount import CreateAccount
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/iHerbMobile")

__author__ = "Tudor C"


class CreateAccountTest17(unittest.TestCase):
    email = "aaa@bbb22.com"
    mobile = "2125552222"
    password = "12345678"
    confirm_password = "password"

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "de9990857cf5"
        desired_caps["appPackage"] = "com.iherb"
        desired_caps["appActivity"] = "com.iherb.navigation.ShopActivity"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_create_account_17(self):
        wait = WebDriverWait(self.driver, 10)
        create = CreateAccount(self.driver)
        # Tap on "Human" icon (right bottom corner)
        create.tap_human_icon_button()
        # Scroll up
        create.scroll_up()
        # Tap on "Sign In" link
        create.tap_signin_link()
        # Tap on "Create an Account" link
        create.tap_create_account_link()
        # Wait until the "Create Account" form is loaded
        create.wait_create_account_form()
        # Enter a valid password in the "Password" field
        create.set_password(self.password)
        # Tap on Password "eye" button
        create.tap_password_eye()
        # Verify if the password can be seen
        element = wait.until(EC.presence_of_element_located((By.XPATH, CreateAccount.password_field))).get_attribute("text")
        assert element == "12345678", "The password cannot be seen."
        # Tap on Password "eye" button
        create.tap_password_eye()
        # Verify if the password was hidden
        element = wait.until(EC.presence_of_element_located((By.XPATH, CreateAccount.password_field))).get_attribute("password")
        assert element == "true", "The password was not hidden."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\iHerbMobile\\Reports",
        report_name="CreateAccountTest17"))
