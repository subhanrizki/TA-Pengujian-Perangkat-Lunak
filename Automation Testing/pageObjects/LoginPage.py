import time
import pytest

class LoginPage:
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    button_login_id = "btnLogin"
    drpdwn_logout_id = "welcome"
    link_logout_xpath = "//*[@id='welcome-menu']/ul/li[3]/a"
    
    def __init__(self,driver):
        self.driver = driver
    
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    
    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    
    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()
    
    def clickLogout(self):
        self.driver.find_element_by_id(self.drpdwn_logout_id).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()
        