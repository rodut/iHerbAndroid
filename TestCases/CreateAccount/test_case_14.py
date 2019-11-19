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


class CreateAccountTest14(unittest.TestCase):
    email = "aaa@bbb22.com"
    mobile = "12345678900"
    password = "password"
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

    def test_create_account_14(self):
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
        # Enter only 11 digits in mobile phone field
        create.set_mobile_number(self.mobile)
        # Enter a valid email address
        create.set_email(self.email)
        # Enter a valid password
        create.set_password(self.password)
        # Confirm the valid password
        create.set_confirm_password(self.confirm_password)
        # Check the "I represent..." checkbox
        create.tap_i_represent_checkbox()
        # Tap on "CREATE AN ACCOUNT" button
        create.tap_create_account_button()
        # Verify if an error message appears ("Please enter a valid phone number")
        element = wait.until(EC.presence_of_element_located((By.XPATH, CreateAccount.invalid_phone_number_3)))
        assert element.is_displayed(), "'Phone number is too short. Please enter a valid phone number' error message appears."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\iHerbMobile\\Reports",
        report_name="CreateAccountTest14"))
