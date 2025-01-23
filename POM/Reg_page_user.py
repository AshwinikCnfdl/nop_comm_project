from selenium.webdriver.common.by import By
class Reg_page_user:
    check_box_male = "gender-male"
    check_box_female = "gender-female"
    text_box_first_name_id = "FirstName"
    text_box_last_name = "LastName"
    text_box_email_id = "Email"
    text_box_pwd_id = "Password"
    text_box_conf_pwd = "ConfirmPassword"
    button_reg_id = "register-button"

    def __init__(self, driver):
        self.driver = driver

    def enter_the_first_name(self, fname):
        self.driver.find_element(By.ID, self.text_box_first_name_id).clear()
        self.driver.find_element(By.ID, self.text_box_first_name_id).send_keys(fname)

    def enter_the_last_name(self, lname):
        self.driver.find_element(By.ID, self.text_box_last_name).clear()
        self.driver.find_element(By.ID, self.text_box_last_name).send_keys(lname)

    def enter_the_email(self, email):
        self.driver.find_element(By.ID, self.text_box_email_id).clear()
        self.driver.find_element(By.ID, self.text_box_email_id).send_keys(email)

    def enter_the_pwd(self, pwd):
        self.driver.find_element(By.ID, self.text_box_pwd_id).clear()
        self.driver.find_element(By.ID, self.text_box_pwd_id).send_keys(pwd)

    def enter_the_cpwd(self, pwd):
        self.driver.find_element(By.ID, self.text_box_conf_pwd).clear()
        self.driver.find_element(By.ID, self.text_box_conf_pwd).send_keys(pwd)

    def click_on_reg_buton(self):
        self.driver.find_element(By.ID, self.button_reg_id).click()

    # validate
    def validate_reg_page_with_title(self, title):
        if "Demo Web Shop. Register" == title:
            assert True
        else:
            assert False

    def validate_user_reg_or_not_title(self, title):
        if "Demo Web Shop. Register" == title:
            assert True
        else:
            assert False
