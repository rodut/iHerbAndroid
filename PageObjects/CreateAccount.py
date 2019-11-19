from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

__author__ = "Tudor C"


class CreateAccount:
    # Locator of all elements
    human_icon = "//android.widget.FrameLayout[@content-desc='Me']/android.widget.ImageView"
    signin_link = "com.iherb:id/text_signin_signout"
    create_account_link = "//android.view.View[@text='Create an Account']"
    create_account_text = "//android.view.View[@text='Create Account']"
    back_arrow_button = "//android.view.View[@text='Login']"
    mobile_number_text = "//android.view.View[@text='Mobile Number']"
    mobile_number_field = "//android.widget.EditText[@resource-id='PhoneNumber']"
    country_code_field = "//android.widget.Spinner[@text='US (+1)']"
    email_address_field = "//android.widget.EditText[@resource-id='Username']"
    password_field = "//android.widget.EditText[@resource-id='Password']"
    confirm_password_field = "//android.widget.EditText[@resource-id='ConfirmPassword']"
    mobile_messaging_text = "//android.view.View[@text='Mobile messaging rates may apply']"
    want_receive_text = "//android.view.View[@text='I want to receive exclusive iHerb Marketing Offers by email, Message Center and app notifications.']"
    represent_that_text_1 = "//android.view.View[@text='I represent that I am 18 years or older and agree to ']"
    represent_that_text_2 = "//android.view.View[@text='and acknowledge I have read iHerb's ']"
    terms_of_use_link = "//android.view.View[@bounds='[268,1008][544,1046]']"
    privacy_policy_link = "//android.view.View[@text='Privacy Policy']"
    create_account_button = "//android.widget.Button[@resource-id='CreateAccount']"
    terms_conditions_page = "//android.view.View[@text='Terms and Conditions']"
    privacy_policy_page = "//android.view.View[@bounds='[32,84][294,134]']"
    invalid_phone_number_1 = "//android.view.View[@text='Please enter a valid phone number']"
    invalid_phone_number_2 = "//android.view.View[@text='Phone number is too short. Please enter a valid phone number']"
    invalid_phone_number_3 = "//android.view.View[@text='Mobile number required to receive the verification code']"
    i_represent_checkbox = "//android.view.View[@bounds='[36,1128][56,1158]']"
    existing_account_error = "//android.view.View[@text='The email address you entered already belongs to an account. Enter another email or sign in']"
    invalid_email_error = "//android.view.View[@text='Please enter a valid username']"
    incorrect_email_error = "//android.view.View[@bounds='[30,320][690,446]']"
    invalid_confirm_pass_error = "//android.view.View[@text='Confirm Password is not valid.']"
    verification_code = "//android.view.View[@text='Enter verification code']"

    def __init__(self, driver):
        self.driver = driver

    def new_confirm_password(self, new_confirm_password):
        self.driver.find_element_by_xpath(self.confirm_password_field).clear()
        self.driver.find_element_by_xpath(self.confirm_password_field).send_keys(new_confirm_password)

    def wait_create_account_form(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.create_account_text)))

    def tap_password_eye(self):
        TouchAction(self.driver).tap(x=642, y=529).perform()

    def tap_confirm_password_eye(self):
        TouchAction(self.driver).tap(x=640, y=654).perform()

    def tap_i_represent_checkbox(self):
        TouchAction(self.driver).tap(x=46, y=994).perform()

    def set_confirm_password(self, confirm_password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.confirm_password_field))).clear().send_keys(confirm_password)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.password_field))).clear().send_keys(password)

    def set_mobile_number(self, mobile):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.mobile_number_field))).clear().send_keys(mobile)

    def set_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.email_address_field))).clear().send_keys(email)

    def tap_create_account_button(self):
        self.driver.find_element_by_xpath(self.create_account_button).click()

    def tap_privacy_policy_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.privacy_policy_link))).click()

    def tap_terms_of_use_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.terms_of_use_link))).click()

    def scroll_down(self):
        self.driver.swipe(100, 1000, 100, 200)

    def scroll_up(self):
        time.sleep(1)
        self.driver.swipe(100, 200, 100, 1000)

    def tap_human_icon_button(self):
        self.driver.find_element_by_xpath(self.human_icon).click()

    def tap_signin_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.signin_link))).click()

    def tap_create_account_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.create_account_link))).click()

    def tap_back_arrow_button(self):
        self.driver.find_element_by_xpath(self.back_arrow_button).click()





