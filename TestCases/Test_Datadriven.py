import time

import pandas as pd
import pytest
from selenium.webdriver.common.by import By
from Configrations.Read_config_file import ReadConfigData
from POM.Home_page_for_user import Home_page_user
from POM.User_login_page import login_page_User
from utilities.CustomLogger import LogGen

def get_test_data(file_path):
    df = pd.read_csv(file_path)
    test_data = []
    for _, row in df.iterrows():
        test_data.append((row["Eamil"], row["pwd"]))
    return test_data

class Test_Data_drivern_teting:
    URL = ReadConfigData.get_demoapplication_url()
    logger1 = LogGen.setup_logger()
    test_data = get_test_data("C:/Users/hp/PycharmProjects/nop_comm_project/TestData/TestData.csv")

    @pytest.mark.sanity
    @pytest.mark.parametrize("email, pwd",test_data)
    def test_login(self, setup,email,pwd):
        self.logger1.info("started test _login_for data driven testing providing the data using parametrize")
        self.logger1.info("open the browser")
        self.driver = setup
        self.driver.get(self.URL)
        self.logger1.info("navigated to url" + self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        hp = Home_page_user(self.driver)
        self.logger1.info("click on the login link ")
        hp.click_on_login_link()
        lp = login_page_User(self.driver)
        lp.enter_the_email_id(email)
        self.logger1.info("enter the email id  " + email)
        lp.enter_the_pwd(pwd)
        self.logger1.info("enter the pwd " + pwd)
        lp.click_on_login_buton()
        self.logger1.info("click on the button ")
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Log out").click()
        self.logger1.info("click on the logout ")

