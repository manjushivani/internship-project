from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import BasePage

class LoginPage(BasePage):
        EMAIL = (By.ID, 'email-2')
        PASSWORD = (By.ID, 'field')
        #LOGIN = (By.XPATH,  "//a[@wized='loginButton']")
        LOGIN = (By.CSS_SELECTOR, "[wized='loginButton']")
        #LOGIN = (By.XPATH, "//a[@class='login-button w-button']")
        VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")
        SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")

        def enter_email(self, email):
            sleep(3)
            self.input_text(email, *self.EMAIL)

        def enter_password(self, password):
            sleep(2)
            self.input_text(password, *self.PASSWORD)

        def enter_continue(self):
            sleep(2)
            self.click(*self.LOGIN)

        def click_secondary_option(self):
            self.click(*self.SECONDARY_OPTION)

        def verify_login(self):
            expected_result = 'Listings'
            actual_result = self.driver.find_element(*self.VERIFY_LOGIN).text
            print(expected_result, actual_result)
            assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
            self.verify_partial_text('Listings', *self.VERIFY_LOGIN)




