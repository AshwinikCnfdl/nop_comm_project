import time
from selenium.webdriver import Chrome
from POM.Login_page import login_page
from Configrations.Read_config_file import ReadConfigData

class Test_login_001:

    URL = ReadConfigData.get_application_url()
    email = ReadConfigData.get_email_id()
    pwd = ReadConfigData.get_pwd()

    def test_login_title(self,setup):
        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.get(self.URL)
        if("Your store. Login" == driver.title):
            assert True
        else:
            assert False

    def test_login(self,setup):
            driver = setup
            driver.maximize_window()
            driver.implicitly_wait(20)
            driver.get(self.URL)
            lp = login_page(driver)
            time.sleep(2)
            lp.click_on_login_buton()
            act_title = driver.title
            print(act_title)
            lp.validate_user_login_or_not_title(act_title)
            time.sleep(5)



