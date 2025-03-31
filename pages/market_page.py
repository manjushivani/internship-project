from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage

class MarketPage(BasePage):

    CLICK_MARKET = By.CSS_SELECTOR, "a[href='/market-companies']"
    MARKET_PAGE = (By.XPATH, '//div[@class="properties-counter agency"]')
    ADD_COMPANY_BTN = (By.CSS_SELECTOR, "a[class='add-company-button w-inline-block']")
    VERIFY_ADD_COMPANY_PAGE= (By.CSS_SELECTOR, "div[class='title-txt-company']")
    PUBLISH_MY_COMPANY_BTN = (By.CSS_SELECTOR, "a[class='publish-button _1 w-button']")

    def click_market(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CLICK_MARKET)).click()

    def verify_right_page(self):
        expected_url = 'https://soft.reelly.io/market-companies'
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'


    def click_company(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.ADD_COMPANY_BTN)).click()

    def verify_add_company_page_opens(self):
        expected_url = 'https://soft.reelly.io/presentation-for-the-agency'
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'


def publish_my_company(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.PUBLISH_MY_COMPANY_BTN)).click()

