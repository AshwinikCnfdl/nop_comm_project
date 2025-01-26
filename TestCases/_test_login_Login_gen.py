import pytest

from Configrations.Read_config_file import ReadConfigData
from POM.Home_page_for_user import Home_page_user
from POM.User_login_page import login_page_User
from utilities.CustomLogger import LogGen

class Test_Loging_Gen_0025:
    URL = ReadConfigData.get_demoapplication_url()
    logger1 = LogGen.setup_logger()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger1.info("Test is staterd Test_login_gen_0025")
        self.driver = setup
        self.driver.get(self.URL)
        self.logger1.info("Open the browser navigated tot" + self.URL)
        self.driver.maximize_window()
        self.logger1.info("max window")
        self.driver.implicitly_wait(20)
        hp = Home_page_user(self.driver)
        self.logger1.info("navigate to home page")
        hp.click_on_login_link()
        self.logger1.info("click on the login button")
        lp = login_page_User(self.driver)
        lp.enter_the_email_id("abc@gmail.com")
        self.logger1.info("enter the user name")
        lp.enter_the_pwd("123456789")
        self.logger1.info("enter the pwd")
        lp.click_on_login_buton()
        self.logger1.info("click on the login button")
        self.logger1.error("demo error")
        self.logger1.warning("demo warring")