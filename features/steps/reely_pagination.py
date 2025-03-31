

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


# @then('Click on Secondary )
# def click_secondary_option(context):
#     context.app.login_page.click_secondary_option()
#
#
# @then('Verify the right page opens')
# def verify_login(context):
#     context.app.login_page.verify_login()
#
# @then('Go to the final page using the pagination button')
# def go_to_pagination(context):
#     context.app.pagination_number.go_to_pagination()
#
# @then('Go back to the first page using the pagination button')
# def go_back_pagination(context):
#     context.app.pagination_number.go_back_pagination()

@then ('Click on “settings” at the left side menu')
def click_settings(context):
    context.app.settings_page.click_settings()
    sleep(1)
@then('Click on the verification option.')
def click_verification(context):
    context.app.settings_page.click_verification()
    sleep(1)
@then('Verify the right page opens')
def verify_right_page(context):
    context.app.settings_page.verify_right_page()
    pass
@then('Verify “upload image”')
def verify_upload_image(context):
    context.app.settings_page.verify_upload_image()

@then('Verify “Next step” buttons are available')
def verify_next_step(context):
    context.app.settings_page.verify_next_step()


    



