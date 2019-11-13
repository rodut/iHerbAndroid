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
__email__ = "tudorache@gmail.com"


class CreateAccountTest21(unittest.TestCase):
    email = "aaa@bb115122.com"
    mobile = "2125552229"
    password = "12345678"
    confirm_password = "12345678"

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "de9990857cf5"
        desired_caps["appPackage"] = "com.iherb"
        desired_caps["appActivity"] = "com.iherb.navigation.ShopActivity"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_create_account_21(self):
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
        # Enter a valid mobile number
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
        # Verify if user was asked for a verification code
        element = wait.until(EC.presence_of_element_located((By.XPATH, CreateAccount.verification_code)))
        assert element.is_displayed(), "Verification code was not asked."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\iHerbMobile\\Reports",
        report_name="CreateAccountTest21"))
