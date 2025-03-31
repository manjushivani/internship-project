from asyncio import timeout

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from pages.base_page import BasePage

class SettingsPage(BasePage):
    #SETTINGS_BTN = (By.XPATH, "//*[@class='w-layout-grid menu_grid']//div[text()='Settings']")
    SETTINGS_BTN = (By.XPATH, "//div[text()='Settings']")
    #VERIFICATION_BTN = (By.XPATH, "//*[@class='page-setting-block w-inline-block']//div[text()='Verification']")
    VERIFICATION_BTN = (By.XPATH, "//div[text()='Verification']")
    #VERIFICATION_PAGE_TITLE = (By.XPATH, "//*[@class='verify-step-block']//div[text()='Upload your photo']")
    VERIFICATION_PAGE_TITLE = (By.XPATH, "//div[text()='Upload your photo']")
    UPLOAD_IMG_BTN = (By.XPATH, "//*[@class='upload-button-2 w-embed']")
    NEXT_STEP_BTN = (By.XPATH, "//a[@wized='nextButtonStep0']//div[text()='Next step ->']")

    # CLICK_SETTINGS = (By.CSS_SELECTOR, "a[href='/settings']")
    # VERIFICATION_BTN = (By.CSS_SELECTOR, "a[href='/verification/step-0']")
    # UPLOAD_IMAGE_BTN = (By.CSS_SELECTOR, "div[class='upload-button-2 w-embed']")
    # NEXT_STEP_BTN = (By.CSS_SELECTOR, "div[class='next-step--']")

    def click_settings(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.SETTINGS_BTN)).click()

    def click_verification(self ):
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.VERIFICATION_BTN)).click()

    def verify_right_page(self  ):
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.VERIFICATION_PAGE_TITLE)).click()

    def verify_upload_image(self):
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.UPLOAD_IMG_BTN)).click()

    def verify_next_step(self):
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.NEXT_STEP_BTN)).click()

#class SettingsPage(Page):
 #     def __init__(self, driver):
 #         super().__init__(driver)
 #
 #     def click_settings_btn(self):
 #         WebDriverWait(self.driver, 10).until(
 #             EC.element_to_be_clickable(CLICK_SETTINGS)
 #         ).click()
 #
 #     def click_verification_btn(self):
 #         WebDriverWait(self.driver, 10).until(
 #             EC.element_to_be_clickable(VERIFICATION_BTN)
 #         ).click()
 #
 #     def verify_right_page(self):
 #         self.verify_url('https://soft.reelly.io/verification/step-0')
 #
 #     def verify_two_btn_available(self):
 #         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(UPLOAD_IMAGE_BTN)
 #                                              )
 #         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(NEXT_STEP_BTN)
 #                                              )
 #
