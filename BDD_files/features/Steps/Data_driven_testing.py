import time

import pandas as pd
import pytest
from Configrations.Read_config_file import ReadConfigData
from POM.Home_page_for_user import Home_page_user
from POM.User_login_page import login_page_User
from utilities.CustomLogger import LogGen
from behave import *
logger = LogGen.setup_logger()

def get_test_data(file_path):
    df = pd.read_csv(file_path)
    test_data = []
    for _, row in df.iterrows():
        test_data.append((row["Eamil"], row["pwd"]))
    return test_data
URL = ReadConfigData.get_demoapplication_url()
logger1 = LogGen.setup_logger()
test_data = get_test_data("C:/Users/hp/PycharmProjects/nop_comm_project/TestData/TestData.csv")

def before_scenario(context, scenario):
    # Read data from Excel file before each scenario
    context.test_data = pd.read_excel('C:/Users/hp/PycharmProjects/nop_comm_project/TestData/TestData.csv')

    # Initialize test variables or other setup
    context.email = context.test_data.iloc[0]['email']
    context.password = context.test_data.iloc[0]['password']

@given(u'open the Chrome browser with url')
def open_the_url(context):
    """ Open browser and navigate to URL """
    logger.info("Opening the browser")
    from selenium import webdriver  # Import WebDriver here to avoid circular import issues
    context.driver = webdriver.Chrome()
    context.driver.get(ReadConfigData.get_demoapplication_url())
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)

@when(u'the user navigates to the login_page')
def click_on_the_login_link(context):
    logger.info("Navigating to login page")
    home_page = Home_page_user(context.driver)
    home_page.click_on_login_link()


@when(u'the user enters email "{email}" and password "{password}" and clicks on login')
@pytest.mark.parametrize("email, pwd", test_data)
def enter_un_and_pwd(context, email, password):
    """Enter the email and password from the feature file and click login"""
    logger.info(f"Entering email: {email}")
    logger.info(f"Entering password: {password}")

    # Find the login page and fill out the credentials
    lp = login_page_User(context.driver)
    lp.enter_the_email_id(email)
    lp.enter_the_pwd(password)
    lp.click_on_login_buton()


@then(u'verify login with set of data results')
def validate_login(context):
   print("login")

