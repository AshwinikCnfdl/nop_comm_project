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
        test_data.append((row["Eamil"], row["pwd"]))
    return test_data

@given(u'open the browser navigate to  url')
def enter_the_url(context):
    logger1.info("Test is Stated BDD with register")
    logger1.info("open the browser")
    context.driver = Chrome()
    context.driver.maximize_window()
    logger1.info("maximize the window")
    context.driver.implicitly_wait(20)
    context.driver.get(URL)
    logger1.info("enter the url" + URL)

@given(u'Click on reg link')
def click_on_the_login(context):
    hp = Home_page_user(context.driver)
    hp.click_on_reg_link()
    logger1.info("click on reg link")

@given(u'enter the "{fn}","{ln}","{email}","{pwd}",cpwd and click on the register')
def enter_all_details(context,fn,ln,email,pwd):
    rp = Reg_page_user(context.driver)
    rp.enter_the_first_name(fn)
    rp.enter_the_last_name(ln)
    rp.enter_the_email(email)
    rp.enter_the_pwd(pwd)
    rp.enter_the_cpwd(pwd)
    logger1.info(f"enter the all details < fn : {fn}, ln : {ln}, email : {email} , pwd : {pwd} , cpwd : {pwd}")
    rp.click_on_reg_buton()

@then(u'verify register results')
def validate_reg(context):
    logger1.info("validate the reg")

#api set up
#sunday grid
