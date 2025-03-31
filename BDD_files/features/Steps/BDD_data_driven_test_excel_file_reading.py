from urllib.error import URLError

import pandas as pd
from selenium.webdriver import Chrome
from behave import *
from Configrations.Read_config_file import ReadConfigData
from POM.Home_page_for_user import Home_page_user
from POM.Reg_page_user import Reg_page_user
from utilities.CustomLogger import LogGen
URL = ReadConfigData.get_demoapplication_url()
logger1 = LogGen.setup_logger()

def get_test_data(file_path,sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    test_data = []
    for _, row in df.iterrows():
        test_data.append((row["FirstName"],row["Last_name"],row["Eamil"], row["pwd"]))
    return test_data

@given(u'open the browser navigate to  url for datadriven')
def enter_the_url(context):
    logger1.info("Test is Stated BDD with register")
    logger1.info("open the browser")
    context.driver = Chrome()
    context.driver.maximize_window()
    logger1.info("maximize the window")
    context.driver.implicitly_wait(20)
    context.driver.get(URL)
    logger1.info("enter the url" + URL)

@given(u'Click on reg link for datadriven')
def click_on_the_login(context):
    hp = Home_page_user(context.driver)
    hp.click_on_reg_link()
    logger1.info("click on reg link")

@given(u'collection_data_from_excel "{location}" and "{sheet_name}"')
def enter_all_details(context, location, sheet_name):
    # Retrieve test data from the specified Excel sheet
    test_data = get_test_data(location, sheet_name)

    # Validate if data is retrieved
    if not test_data:
        logger1.error(f"No test data found in '{sheet_name}' of '{location}'.")
        return

    # Instantiate the Registration Page object
    rp = Reg_page_user(context.driver)

    # Iterate through test data and perform actions
    for fn, ln, email, pwd in test_data:
        rp.enter_the_first_name(fn)
        rp.enter_the_last_name(ln)
        rp.enter_the_email(email)
        rp.enter_the_pwd(pwd)
        rp.enter_the_cpwd(pwd)
        # Log entered data (excluding sensitive details for security reasons)
        logger1.info(f"Entered details: <First Name: {fn}, Last Name: {ln}, Email: {email}>")
        # Perform registration action
        rp.click_on_reg_buton()


@then(u'verify register results for data driven')
def validate_reg(context):
    logger1.info("validate the reg")

#api set up
#sunday grid
