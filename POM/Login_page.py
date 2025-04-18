from selenium.webdriver.common.by import By
class login_page:
    __text_box_email_id = "Email"
    __text_box_pwd_id = "Password"
    __check_box_rember_me_id = "RememberMe"
    __button_login_xpath = "//button[text()='Log in']"
    __button_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def enter_the_email_id(self, email):
        self.driver.find_element(By.ID, self.__text_box_email_id).clear()
        self.driver.find_element(By.ID, self.__text_box_email_id).send_keys(email)

    def enter_the_pwd(self, pwd):
        self.driver.find_element(By.ID, self.__text_box_pwd_id).clear()
        self.driver.find_element(By.ID, self.__text_box_pwd_id).send_keys(pwd)

    def click_on_login_buton(self):
        self.driver.find_element(By.XPATH, self.__button_login_xpath).click()

    def click_on_rember_me(self):
        self.driver.find_element(By.ID, self.__check_box_rember_me_id).click()

    def click_on_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.__button_logout_link_text).click()

    # validate
    def validate_login_page_with_title(self, title):
        if "Your store. Login" == title:
            return True
        else:
            return False

    def validate_user_login_or_not_title(self, title):
        if "Dashboard / nopCommerce administration" == title:
            assert True
        else:
            assert False
