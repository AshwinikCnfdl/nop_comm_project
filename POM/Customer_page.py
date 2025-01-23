from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Customer_moulde_serach_customer:
    email_text_box_id = "SearchEmail"
    first_name_text_box_id  = "SearchFirstName"
    last_name_text_box_id = "SearchLastName"
    drop_down_month_id = "SearchMonthOfBirth"
    drop_down_Day_id = "SearchDayOfBirth"
    RegistrationDatefrom_text_box_id = "SearchRegistrationDateFrom"
    RegistrationDateTo_text_box_id = "SearchRegistrationDateTo"
    LastActivityFrom_text_box_id = "SearchLastActivityFrom"
    LastActivityTo_text_box_id = "SearchLastActivityTo"
    company_text_box_id = "SearchCompany"
    ip_add_text_box = "SearchIpAddress"
    customer_role_text_box = "//ul[@class='select2-selection__rendered']"
    serach_button_id = "search-customers"
    add_new_customer_button_xpath = "//a[@class='btn btn-primary']"
    export_button_xpath = "(//button[@type='button'])[2]"
    import_button_xpath = "(//button[@type='button'])[6]"
    edit_customer_xpath = "(//i[@class='fas fa-pencil-alt'])[1]"

    # action methods

    def __init__(self,driver):
        self.driver = driver

    def enter_the_serach_email_id(self,email):
        self.driver.find_element(By.ID, self.email_text_box_id).clear()
        self.driver.find_element(By.ID, self.email_text_box_id).send_keys(email)

    def enter_serach_first_name(self,fn):
        self.driver.find_element(By.ID, self.first_name_text_box_id).clear()
        self.driver.find_element(By.ID, self.first_name_text_box_id).send_keys(fn)

    def enter_serach_last_name(self,ln):
        self.driver.find_element(By.ID, self.last_name_text_box_id).clear()
        self.driver.find_element(By.ID, self.last_name_text_box_id).send_keys(ln)

    def select_month_by_text(self,text):
        month = self.driver.find_element(By.ID,"drop_down_month_id")
        select = Select(month)
        select.select_by_visible_text(text)

    def select_day_by_text(self,text):
        day = self.driver.find_element(By.ID,"drop_down_Day_id")
        select = Select(day)
        select.select_by_visible_text(text)

    def enter_reg_date_from(self,date):
        """date from mate = dd-mm-yyyy"""
        self.driver.find_element(By.ID, self.RegistrationDatefrom_text_box_id).clear()
        self.driver.find_element(By.ID, self.RegistrationDatefrom_text_box_id).send_keys(date)
    def enter_reg_date_to(self,date):
        """date from mate = dd-mm-yyyy"""
        self.driver.find_element(By.ID, self.RegistrationDateTo_text_box_id).clear()
        self.driver.find_element(By.ID, self.RegistrationDateTo_text_box_id).send_keys(date)
    def enter_active_from(self,date):
        """date from mate = dd-mm-yyyy"""
        self.driver.find_element(By.ID, self.LastActivityFrom_text_box_id).clear()
        self.driver.find_element(By.ID, self.LastActivityFrom_text_box_id).send_keys(date)
    def enter_active_to(self,date):
        """date from mate = dd-mm-yyyy"""
        self.driver.find_element(By.ID, self.LastActivityTo_text_box_id).clear()
        self.driver.find_element(By.ID, self.LastActivityTo_text_box_id).send_keys(date)

    def enter_customer_company(self,complany):
        self.driver.find_element(By. ID.company_text_box_id).clear()
        self.driver.find_element(By.ID.company_text_box_id).send_keys(complany)




