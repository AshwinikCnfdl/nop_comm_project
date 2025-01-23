import time

import pytest
from selenium.webdriver import Chrome
from POM.Home_page_for_user import Home_page_user
from POM.Login_page import login_page
from Configrations.Read_config_file import ReadConfigData
from POM.Reg_page_user import Reg_page_user
from utilities.Write_test_data import Read_write_csv_file
from utilities.CustomLogger import LogGen
import random
import string
from faker import Faker

class Test_Reg_001:
    # Test setup
    URL = ReadConfigData.get_demoapplication_url()
    logger1 = LogGen.log_gen()

    @pytest.mark.regration
    def test_Home_title(self, setup):
        self.logger1.info("*************** Test_Reg_001: Verifying Home Page Title ***************")

        driver = setup
        try:
            self.logger1.info("Launching the browser and navigating to the application URL.")
            driver.maximize_window()
            driver.implicitly_wait(20)
            driver.get(self.URL)

            self.logger1.info("Fetching the page title for validation.")
            actual_title = driver.title
            expected_title = "Demo Web Shop"

            if actual_title == expected_title:
                self.logger1.info(f"Home page title validation passed. Title: '{actual_title}'")
                assert True
            else:
                self.logger1.error(
                    f"Home page title validation failed. Expected: '{expected_title}', Found: '{actual_title}'")
                assert False, f"Title mismatch. Expected: '{expected_title}', Found: '{actual_title}'"

        except Exception as e:
            self.logger1.error(f"An exception occurred during the test: {str(e)}")
            assert False, f"Test failed due to an exception: {str(e)}"

        finally:
            self.logger1.info("Closing the browser.")
            driver.quit()

    def generate_random_email(self):
        """Generate a random email address."""
        domains = ["gmail.com", "yahoo.com", "outlook.com"]
        random_domain = random.choice(domains)
        random_user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{random_user}@{random_domain}"

    def generate_random_password(self):
        """Generate a random password."""
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(chars, k=10))

    def generate_rondom_first_name(self):
        char = string.ascii_letters
        return ''.join(random.choices(char,k = 8))

    def generate_rondom_last_name(self):
        char = string.ascii_letters
        return ''.join(random.choices(char, k=3))

    @pytest.mark.sanity
    @pytest.mark.regration
    def test_Reg(self,setup):
            pwd = self.generate_random_password()
            fn = self.generate_rondom_first_name()
            ln = self.generate_rondom_last_name()
            email = self.generate_random_email()
            driver = setup
            driver.maximize_window()
            driver.implicitly_wait(20)
            driver.get(self.URL)
            hp = Home_page_user(driver)
            hp.click_on_reg_link()
            rp = Reg_page_user(driver)
            rp.validate_reg_page_with_title(driver.title)
            rp.enter_the_first_name(fn)
            rp.enter_the_last_name(ln)
            rp.enter_the_email(email)
            rp.enter_the_pwd(pwd)
            rp.enter_the_cpwd(pwd)
            rp.click_on_reg_buton()
            rp.validate_user_reg_or_not_title(driver.title)
            data = {
                'FirstName': [fn],
                'Last_name': [ln],
                'Eamil': [email],
                'pwd' :[pwd],
                'cpwd' :[pwd]
            }

            Read_write_csv_file.write_test_data(data)
            time.sleep(20)











