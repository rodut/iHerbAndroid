import unittest
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjects.CreateAccount import CreateAccount
import sys
sys.path.append("C:/Users/Tudor/PycharmProjects/iHerbMobile")

__author__ = "Tudor C"
__email__ = "tudorache@gmail.com"


class CreateAccountTest04(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "de9990857cf5"
        desired_caps["appPackage"] = "com.iherb"
        desired_caps["appActivity"] = "com.iherb.navigation.ShopActivity"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_create_account_04(self):
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
        # Verify if "Mobile messaging rates may apply" text is displayed
        element = wait.until(EC.presence_of_element_located((By.XPATH, CreateAccount.mobile_messaging_text)))
        assert element.is_displayed(), "'Mobile messaging rates may apply' text is displayed."


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="C:\\Users\\Tudor\\PycharmProjects\\iHerbMobile\\Reports",
        report_name="CreateAccountTest04"))
