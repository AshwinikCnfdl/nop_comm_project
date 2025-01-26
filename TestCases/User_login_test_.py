import time

import pytest
from selenium.webdriver.common.by import By
from Configrations.Read_config_file import ReadConfigData
from POM.Home_page_for_user import Home_page_user
from POM.User_login_page import login_page_User
from utilities.CustomLogger import LogGen
from utilities.Write_test_data import Read_write_csv_file

class Test_Cases_login_user_004:
    URL = ReadConfigData.get_demoapplication_url()
    logger1 = LogGen.setup_logger()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver = setup
        df = Read_write_csv_file.read_test_data("C:/Users/hp/PycharmProjects/nop_comm_project/TestData/TestData.csv")
        email = df["Eamil"]
        pwd = df["pwd"]
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        hp = Home_page_user(self.driver)
        hp.click_on_login_link()
        lp = login_page_User(self.driver)
        lp.enter_the_email_id(email.iloc[0])
        lp.enter_the_pwd(pwd.iloc[0])
        lp.click_on_login_buton()
        for i in range(0, len(df)):
            self.driver.find_element(By.LINK_TEXT, "Log out").click()
            hp = Home_page_user(self.driver)
            hp.click_on_login_link()
            lp = login_page_User(self.driver)
            lp.enter_the_email_id(email.iloc[i])
            lp.enter_the_pwd(pwd.iloc[i])
            lp.click_on_login_buton()

        # time.sleep(50)
# report //log file
# par
#Failed Test
# taking the screenshot
# grid  docker :--4 Data API

#driver = setup
#-browser pytest -s -v -n auto TestCases/Reg_uer_Test_.py - Firefox
# pytest -s -v -n auto TestCases/Reg_uer_Test_.py --browser =Firefox
# pytest -s -v -n 1 --html=Reports/report.html TestCases/User_login_test_.py --browser=Chrome
# grouping the testcases
# taking sc report
# more num testcases
# grid #dockers
#pytest -s -v -m 'sanity' --html=Reports/report.html TestCases/ --browser=Chrome
#pytest -s -v -m 'sanity' --html=Reports/report.html TestCases/Reg_uer_Test_.py --browser=Chrome