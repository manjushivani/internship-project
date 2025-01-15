from selenium.webdriver.common.by import By
from symtable import Class
from time import sleep

from pages.base_page import BasePage
#class LoginPage(BasePage):

    # def login(self):
    #     self.login_account(email='<EMAIL>', password='<PASSWORD>')
    #     #self.click(#*self,#continuebutton)
    #     sleep(2)
class LoginPage(BasePage):
        EMAIL = (By.ID, 'email-2')
        PASSWORD = (By.ID, 'field')
        LOGIN = (By.XPATH,  "//a[@wized='loginButton']")
        VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")

        # def enter_email(self, email):
        # self.input_text(*self.EMAIL)
        def enter_email(self, email):
            self.input_text(email, *self.EMAIL)
            #self.send_keys('manjuk25@hotmail.com')

        # def enter_email(self, email):
        # self.input_text(self, *self.EMAIL)
        # self.input_text(self,text'samha1n@encouragesless.site', *EMAIL)
        def enter_password(self, password):
            self.input_text(password, *self.PASSWORD)
            sleep(2)

        def enter_login(self):
            self.click(*self.LOGIN)
            sleep(2)


        def verify_login(self):
            self.verify_partial_text('Listings', *self.VERIFY_LOGIN)
            sleep(2)

