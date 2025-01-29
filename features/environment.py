from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options
from support.logger import logger


from app.application import Application

#def browser_init(context,scenario_name):
def browser_mobile_init(context):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()

    # Set up Chrome options for mobile emulation

    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #context.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',options=chrome_options)

    # # Google chrome
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    # ### BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'manju_DHOswR'
    # bs_key = 'YByBWFwxDMxeFqThA3SF'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # #
    # options = Options()
    # bstack_options = {
    #     #"os": "Windows",
    #     #"osVersion": "11",
    #     #'browserName': 'edge',
    #     # "os": "OS X",
    #     # "osVersion": "Monterey",
    #     # 'browserName': 'Safari',
    #     # 'browserVersion': 15.6,
    #     # 'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ## Firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # firefox_options = Options()
    # context.driver = webdriver.Firefox(service=service, options=firefox_options)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)
#def before_scenario(context, scenario):
def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #browser_init(context,scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    #browser_init(context)
    browser_mobile_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')

def after_scenario(context, feature):
       # Add browser logs:
    # browser_logs = context.driver.get_log('browser')
    # with open("browser_logs.txt", "w") as log_file:
    #     for log_entry in browser_logs:
    #         log_file.write(f"{log_entry['level']} - {log_entry['timestamp']} - {log_entry['message']}\n")
    # print("Browser logs have been saved to browser_logs.txt")
    context.driver.quit()