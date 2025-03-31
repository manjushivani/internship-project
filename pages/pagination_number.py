from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import BasePage

class PaginationNumber(BasePage):

    TOTAL_PAGES_NUMBER = (By.CSS_SELECTOR, "[wized='totalPageProperties']")
    LAST_PAGE_ARROW_BUTTON = (By.CSS_SELECTOR, "[wized='nextPageMLS']")
    FIRST_PAGE_ARROW_BUTTON = (By.CSS_SELECTOR, "[wized='previousPageMLS']")
    CURRENT_PAGE = (By.CSS_SELECTOR, "[wized='currentPageProperties']")


    def go_to_pagination(self, *locator):
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES_NUMBER).text)
        current_page = int(self.driver.find_element(*self.CURRENT_PAGE).text)

        print(f"Total pages: {total_pages}")
        print(f"Current page: {current_page}")

        # Navigate through all pages using a for loop
        for page in range(1, total_pages + 1):

            wait = WebDriverWait(self.driver, 25)
            sleep(6)

            print(f"Successfully loaded page {page}.")
            if page != total_pages:

                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                last_page_arrow_button = wait.until(EC.visibility_of_element_located(self.LAST_PAGE_ARROW_BUTTON))
                last_page_arrow_button.click()

            print("Successfully reached the next page.")

        current_page_after_loop = int(self.driver.find_element(*self.CURRENT_PAGE).text)

        print(f"Current pages after loop: {current_page_after_loop}")

        assert current_page_after_loop == total_pages, 'Did not reach last page'
        print("Pagination testing completed successfully!")


    def go_back_pagination(self, *locator):
        #self.driver.execute_script("window.scrollBy(0,2000)", "")
        # self.driver.find_element(*locator).click()
        sleep(6)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES_NUMBER).text)
        current_page = int(self.driver.find_element(*self.CURRENT_PAGE).text)

        print(f"Total pages: {total_pages}")
        print(f"Current page: {current_page}")

        # Navigate through all pages using a for loop
        for page in range(total_pages,0, - 1):

            wait = WebDriverWait(self.driver, 25)
            sleep(6)

            print(f"Successfully loaded page {page}.")
            if page != 1:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                wait = WebDriverWait(self.driver, 20)
                first_page_arrow_button = wait.until(EC.visibility_of_element_located(self.FIRST_PAGE_ARROW_BUTTON))
                first_page_arrow_button.click()

            print("Successfully reached the next page.")

        current_page = int(self.driver.find_element(*self.CURRENT_PAGE).text)

        print(f"Current pages after loop: {current_page}")

        assert current_page == 1, 'Did not reach first page'
        print("Pagination testing completed successfully!")

