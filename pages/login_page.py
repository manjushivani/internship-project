from selenium.webdriver.common.by import By
from symtable import Class
from time import sleep

from pages.base_page import BasePage

class LoginPage(BasePage):
        EMAIL = (By.ID, 'email-2')
        PASSWORD = (By.ID, 'field')
        LOGIN = (By.XPATH,  "//a[@wized='loginButton']")
        VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")
        SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")

        def enter_email(self, email):
            self.input_text(email, *self.EMAIL)

        def enter_password(self, password):
            self.input_text(password, *self.PASSWORD)
            sleep(2)

        def enter_login(self):
            self.click(*self.LOGIN)
            sleep(2)

        def verify_login(self):
            expected_result = 'Listings'
            actual_result = self.driver.find_element(*self.VERIFY_LOGIN).text
            print(expected_result, actual_result)
            assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
            self.verify_partial_text('Listings', *self.VERIFY_LOGIN)
            sleep(2)

        def click_secondary_option(self):
            self.click(*self.SECONDARY_OPTION)

