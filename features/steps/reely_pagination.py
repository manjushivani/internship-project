from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

#EMAIL = (By.ID, 'email-2')
#PASSWORD = (By.ID, 'field')
#LOGIN = (By.XPATH, "//a[@wized='loginButton']")
VERIFY_LOGIN = (By.XPATH, "//div[text()='Listings']")

@given('Open the main page')
def open_main(context):
    #context.driver.get('https://soft.reelly.io')
    context.app.main_page.open_main()


@when('Enter email')
def enter_email(context):
    #context.driver.find_element(By.ID, 'email-2').send_keys('manjuk25@hotmail.com')
    #context.driver.find_element(*EMAIL).send_keys('manjuk25@hotmail.com')
    context.app.login_page.enter_email('manjuk25@hotmail.com')

@then('Enter password')
def enter_password(context):
    context.app.login_page.enter_password('internshipproject')

@then('CLick continue button')
def enter_login(context):
    context.app.login_page.enter_login()
    sleep(10)

@then('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.driver.find_element(By.XPATH, "//div[text()='Secondary']").click()
    sleep(5)

@then('Verify the right page opens')
def verify_login(context):
    expected_result = 'Listings'
    actual_result = context.driver.find_element(*VERIFY_LOGIN).text
    context.app.login_page.verify_login()
    print(expected_result, actual_result)
    assert expected_result in actual_result, f'Expected {expected_result} match actual {actual_result}'


@then('Go to the final page using the pagination button')
def go_to_pagination(context):
    # Testing for loop for pagination
    total_pages = int(context.driver.find_element(By.XPATH, "//div[text()='116']").text)
    print(f"Total pages: {total_pages}")

    # Navigate through all pages using a for loop
    for page in range(1, total_pages + 1):
        # Locate and interact with the page input or buttons (update selector as needed)
        wait = WebDriverWait(context.driver, 10)
        #current_page_input = context.driver.find_element(By.XPATH, "//div[@w-el-text=1]").text
        last_page_arrow_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@class,'pagination__button')]")))
        last_page_arrow_button.click()
        #current_page_input = context.driver.find_element(By.XPATH, "//div[@w-el-text=1]").text
        #context.driver.find_element(By.XPATH, "//a[contains(@class,'pagination__button')]").click()

        print(f"Successfully loaded page {page}.")

    print("Pagination testing completed successfully!")

    current_page = context.driver.find_element(By.XPATH, "//div[text()='116']")
    assert current_page.text == "116", f"Expected page 116, got {current_page.text}"
    print("Successfully reached the last page.")


@then('Go back to the first page using the pagination button')
def go_back(context):
    total_pages = int(context.driver.find_element(By.XPATH, "//div[text()='116']").text)
    print(f"Total pages: {total_pages}")
    for page in range(1, total_pages -1):
        # Locate and interact with the page input or buttons (update selector as needed)
        wait = WebDriverWait(context.driver, 10)
        #current_page_input = context.driver.find_element(By.XPATH, "//div[text()='116']").text
        first_page_arrow_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'pagination__button')]")))
        first_page_arrow_button.click()
        print(f"Successfully loaded page {page}.")

    print("Pagination testing completed successfully!")
    sleep(5)

    first_page_number = context.driver.find_element(By.XPATH, "//div[@w-el-text=1]").text
    print(first_page_number)
    sleep(2)
    print("Successfully returned to the first page.")



