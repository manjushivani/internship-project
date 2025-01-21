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

    #def click(self, *locator):
    def click(self, locator):
        #self.driver.find_element(*locator).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
        #return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).text

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def text(self, *locator):
        return self.driver.find_element(*locator).text

    def get_current_window_handle(self):
        window = self.driver.current_window_handle
        print('Current window ', window)
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print('All windows: ', all_windows)
        self.driver.switch_to.window(all_windows[1])
        print('Current window ', self.driver.current_window_handle)

    def switch_to_window_by_id(self, window_id):
        self.driver.switch_to.window(window_id)
        print('Current window ', self.driver.current_window_handle)

    def wait_for_element_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def wait_for_element_invisible(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} should not be visible'
        )

    def wait_for_element_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        )

    def wait_and_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in actual {actual_text}'

    def close(self):
        self.driver.close()

