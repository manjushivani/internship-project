

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def send_keys(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    # def login_account(self, email, password):
    #     self.driver.find_element_by_id('email').send_keys(email)
    #     self.driver.find_element_by_id('password').send_keys(password)


    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)


    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


    def text(self, *locator):
        return self.driver.find_element(*locator).text

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

    # def get_current_window_handle(self):
    #     window = self.driver.current_window_handle
    #     print('Current window ', window)
    #     return window
    #
    # def switch_to_new_window(self):
    #     #self.wait.until(EC.new_window_is_opened)
    #     all_windows = self.driver.window_handles
    #     print('All windows: ', all_windows)
    #     self.driver.switch_to.window(all_windows[1])
    #     print('Current window ', self.driver.current_window_handle)
    #
    # def switch_to_window_by_id(self, window_id):
    #     self.driver.switch_to.window(window_id)
    #     print('Current window ', self.driver.current_window_handle)

    def close(self):
        self.driver.close()

