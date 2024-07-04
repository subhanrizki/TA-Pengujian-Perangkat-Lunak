import pytest
import time
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_001_Login:
    
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    
    logger = LogGen.loggen()
    
    def test_homePageTitle(self,setup):
        
        self.driver = setup
        self.logger.info("**********Starting Test_001_Login**********")
        self.logger.info("********** WebTitle Test Started ***********")
        self.logger.info("***** Launching Browser *****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("***** Checking the Title of the WebPage *****")
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            self.logger.info("***** Congrats!! Title is matching, Closing Browser *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\orangeHRM\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.info("***** OOPS!! Title is not matching, Closing Browser *****")
            self.driver.close()
            assert False
    
    def test_login(self,setup):
        
        self.driver = setup
        self.logger.info("************ Opening OrangeHRM Application ************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("***** Checking the Login Functionality *****")
        self.lp = LoginPage(self.driver)
        time.sleep(2)
        self.logger.info("***** Entering UserName *****")
        self.lp.setUserName(self.username)
        self.logger.info("***** Entering Password *****")
        self.lp.setPassword(self.password)
        self.logger.info("***** Clicking on Login Button *****")
        self.lp.clickLogin()
        act_url = self.driver.current_url
        
        if act_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
            self.logger.info("***** Logged in Successfully *****")
            self.lp.clickLogout()
            self.logger.info("***** Closing Browser *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\orangeHRM\\Screenshots\\"+"LoginFailed.png")
            self.logger.info("***** Login Failed, Please check the Screenshots Folder *****")
            self.driver.close()
            self.logger.info("***** Closing Browser *****")
            assert False
    
    