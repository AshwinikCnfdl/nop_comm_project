import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from Configrations.Read_config_file import ReadConfigData
from POM.Home_page_for_user import Home_page_user
from POM.User_login_page import login_page_User
from utilities.CustomLogger import LogGen

# Logger Setup
logger = LogGen.setup_logger()


@given("open the browser")
def open_browser(context):
    """ Open browser and navigate to URL """
    logger.info("Opening the browser")
    from selenium import webdriver  # Import WebDriver here to avoid circular import issues
    context.driver = webdriver.Chrome()
    context.driver.get(ReadConfigData.get_demoapplication_url())
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@when("the user navigates to the login page")
def click_on_the_login_link(context):
    """ Clicks on the login link """
    logger.info("Navigating to login page")
    home_page = Home_page_user(context.driver)
    home_page.click_on_login_link()


@when('the user enters  email and password and click on login')
def enter_credentials_and_login(context):
    lp = login_page_User(context.driver)
    lp.enter_the_email_id("abc@gmail.com")
    lp.enter_the_pwd("123456789")
    lp.click_on_login_buton()

    time.sleep(5)  # Temporary wait to allow page load


@then("verify login results")
def verify_login(context):
    logger.info("User logged out successfully")
time.sleep(50)