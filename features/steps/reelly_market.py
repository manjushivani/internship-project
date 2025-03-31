from behave import  then
from time import sleep

@then ('Click on “Market” at the left side menu.')
def click_market(context):
    context.app.market_page.click_market()


@then ('Verify the right page opens.')
def verify_right_page(context):
    context.app.market_page.verify_right_page()


@then ('Click on “Add Company” button.')
def click_company(context):
    context.app.market_page.click_company()


@then ('Verify the right page opens for market.')
def verify_add_company_page_opens(context):
    context.app.market_page.verify_add_company_page_opens()


@then ('Verify the button “Publish my company” is available.')
def publish_my_company(context):
    context.app.market_page.publish_company()

