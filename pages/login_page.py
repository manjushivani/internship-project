from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
            #sleep(3)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.EMAIL)).is_displayed()
            self.input_text(email, *self.EMAIL)

        def enter_password(self, password):
            #sleep(2)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD)).is_displayed()
            self.input_text(password, *self.PASSWORD)

        def enter_continue(self):
            #self.click(*self.LOGIN)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN)).click()

        def click_secondary_option(self):
            #sleep(2)
            #self.click(*self.SECONDARY_OPTION)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SECONDARY_OPTION)).click()

        def verify_login(self):
            #sleep(2)
            expected_result = 'Listings'
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.VERIFY_LOGIN)).is_displayed()
            actual_result = self.driver.find_element(*self.VERIFY_LOGIN).text
            print(expected_result, actual_result)
            assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'
            self.verify_partial_text('Listings', *self.VERIFY_LOGIN)




