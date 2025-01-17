from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import BasePage

class PaginationNumber(BasePage):
    TOTAL_PAGES_NUMBER = (By.XPATH, "//div[text()='116']")
    LAST_PAGE_ARROW_BUTTON = (By.XPATH, "//a[contains(@class,'pagination__button')]")
    FIRST_PAGE_ARROW_BUTTON = (By.XPATH, "//div[contains(@class,'pagination__button')]")

    def go_to_pagination(self, *locator):
        #self.driver.find_element(*locator).click()

        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES_NUMBER).text)
        print(f"Total pages: {total_pages}")

        # Navigate through all pages using a for loop
        for page in range(1, total_pages + 1):
            # Locate and interact with the page input or buttons (update selector as needed)
            wait = WebDriverWait(self.driver, 10)
            # current_page_input = context.driver.find_element(By.XPATH, "//div[@w-el-text=1]").text
            last_page_arrow_button = wait.until(EC.visibility_of_element_located(self.LAST_PAGE_ARROW_BUTTON))
            last_page_arrow_button.click()
            # current_page_input = context.driver.find_element(By.XPATH, "//div[@w-el-text=1]").text
            # context.driver.find_element(By.XPATH, "//a[contains(@class,'pagination__button')]").click()

            print(f"Successfully loaded page {page}.")

        print("Pagination testing completed successfully!")

        current_page = self.driver.find_element(*self.TOTAL_PAGES_NUMBER)
        assert current_page.text == "116", f"Expected page 116, got current_page"
        print("Successfully reached the last page.")

    def go_back_pagination(self, *locator):
        #self.driver.find_element(*locator).click()
        total_pages = int(self.driver.find_element(*self.TOTAL_PAGES_NUMBER).text)
        print(f"Total pages: {total_pages}")

        for page in range(1, total_pages - 1):
            # Locate and interact with the page input or buttons (update selector as needed)
            wait = WebDriverWait(self.driver, 10)
            # current_page_input = context.driver.find_element(By.XPATH, "//div[text()='116']").text
            first_page_arrow_button = wait.until(EC.visibility_of_element_located(self.FIRST_PAGE_ARROW_BUTTON))
            first_page_arrow_button.click()
            print(f"Successfully loaded page {page}.")

        print("Pagination testing completed successfully!")
        sleep(5)

        first_page_number = self.driver.find_element(By.XPATH, "//div[@w-el-text=1]").text
        print(first_page_number)
        sleep(2)
        print("Successfully returned to the first page.")
