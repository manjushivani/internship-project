from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# EMAIL = (By.ID, 'email-2')
# PASSWORD = (By.ID, 'field')
# LOGIN = (By.XPATH, "//a[@wized='loginButton']")
# VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")
# SECONDARY_OPTION = (By.XPATH, "//div[text()='Secondary']")
# TOTAL_PAGES_NUMBER = (By.XPATH, "//div[text()='116']")
# LAST_PAGE_ARROW_BUTTON =(By.XPATH, "//a[contains(@class,'pagination__button')]")
# FIRST_PAGE_ARROW_BUTTON = (By.XPATH, "//div[contains(@class,'pagination__button')]")

@given('Open the main page')
def open_main(context):
    context.app.main_page.open_main()

@when('Enter email')
def enter_email(context):
    context.app.login_page.enter_email('manjuk25@hotmail.com')

@then('Enter password')
def enter_password(context):
    context.app.login_page.enter_password('internshipproject')

@then('CLick continue button')
def enter_continue(context):
    context.app.login_page.enter_continue()


@then('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.login_page.click_secondary_option()


@then('Verify the right page opens')
def verify_login(context):
    context.app.login_page.verify_login()

@then('Go to the final page using the pagination button')
def go_to_pagination(context):
    context.app.pagination_number.go_to_pagination()

@then('Go back to the first page using the pagination button')
def go_back_pagination(context):
    context.app.pagination_number.go_back_pagination()




