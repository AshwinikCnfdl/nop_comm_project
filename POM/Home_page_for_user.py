from selenium.webdriver.common.by import By

class Home_page_user:
    reg_link = "Register"
    login_link = "Log in"
    shopping_cart_link = "Shopping cart"
    text_serach_box_id = "small-searchterms"
    button_serach_xpath= "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_reg_link(self):
        self.driver.find_element(By.LINK_TEXT,self.reg_link).click()

    def click_on_login_link(self):
        self.driver.find_element(By.LINK_TEXT,self.login_link).click()

    def click_on_shopping_cart(self):
        self.driver.find_element(By.LINK_TEXT,self.shopping_cart_link).click()

    def enter_the_serach_item(self, item):
        self.driver.find_element(By.ID, self.text_serach_box_id).clear()
        self.driver.find_element(By.ID, self.text_serach_box_id).send_keys(item)

    def click_on_serach_button(self):
        self.driver.find_element(By.XPATH,self.button_serach_xpath).click()