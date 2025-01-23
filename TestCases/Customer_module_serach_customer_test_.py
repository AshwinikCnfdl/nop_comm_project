import time

from selenium.webdriver import Chrome


from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from POM.Customer_page import Customer_moulde_serach_customer
from POM.Login_page import login_page


class Test_serach_Customer_Tc002:
    #https://admin-demo.nopcommerce.com/Admin/Customer/List

    driver = Chrome()
    def test_login(self,setup):
            driver = setup
            driver.maximize_window()
            driver.implicitly_wait(20)
            driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
            lp = login_page(driver)
            time.sleep(2)
            lp.click_on_login_buton()
            act_title = driver.title
            print(act_title)
            lp.validate_user_login_or_not_title(act_title)
            time.sleep(5)
    def test_customer_serah(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        self.driver.maximize_window()
        self.driver.implicitly_wait(50)
        csp = Customer_moulde_serach_customer(self.driver)
        csp.enter_the_serach_email_id("kiyjcycyhjc676008@gmail.com")
        csp.enter_serach_first_name("Virat Kohli")
        csp.enter_serach_last_name("K")
        csp.select_day_by_text("12")
        csp.select_day_by_text("10")
        csp.enter_reg_date_from("15-10-2024")
        csp.enter_reg_date_to("10-07-2024")
        csp.enter_active_from("15-10-2024")
        csp.enter_active_to("10-07-2024")
        csp.enter_customer_company("new")



