from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.market_page import MarketPage
from pages.pagination_number import PaginationNumber
from pages.settings_page import  SettingsPage


class Application:

    def __init__(self,driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.pagination_number = PaginationNumber(driver)
        self.settings_page =SettingsPage(driver)
        self.market_page = MarketPage(driver)



