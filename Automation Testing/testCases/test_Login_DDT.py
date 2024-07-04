import pytest
import time
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import ExcelUtils

class Test_002_Login:
    
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    path = '.\\TestData\\OrangeLoginData.xlsx'
    lst_status = []
    
    
    def test_login(self,setup):
        
        self.driver = setup
        self.logger.info("*********** Starting TEST_002_Login_DDT ***********")
        self.logger.info("************ Opening OrangeHRM Application ************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("***** Checking the Login Functionality with multiple users *****")
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,"Sheet1")
        for r in range(2,self.rows+1):
            self.logger.info("***** Entering "+ str(r-1) +" UserName *****")
            self.lp.setUserName(ExcelUtils.readData(self.path,"Sheet1",r,1))
            self.logger.info("***** Entering Password *****")
            self.lp.setPassword(ExcelUtils.readData(self.path,"Sheet1",r,2))
            self.logger.info("***** Clicking on Login Button *****")
            self.lp.clickLogin()
            time.sleep(2)
            act_url = self.driver.current_url
            self.expected_condition = ExcelUtils.readData(self.path,"Sheet1",r,3)
            
            if act_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
                if self.expected_condition == "Pass":
                    self.logger.info("***** Expected Condition met successfully *****")
                    self.lst_status.append("Pass")
                    self.lp.clickLogout()
                    
                elif self.expected_condition == "Fail":
                    self.logger.info("***** Expected Condition not met *****")
                    self.lst_status.append("Fail")
                    self.lp.clickLogout()
                    
            elif act_url!= "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
                if self.expected_condition == "Pass":
                    self.logger.info("***** Failed *****")
                    self.driver.save_screenshot("C:\\Users\\Salim\\eclipse-workspace\\orangeHRM\\Screenshots\\"+"LoginFailed"+str(r-1)+".png")
                    self.logger.info("***** Login Failed, Please check the Screenshots Folder *****")
                    self.lst_status.append("Fail")
                    
                elif self.expected_condition == "Fail":
                    self.logger.info("***** Expected Condition met successfully *****")
                    self.lst_status.append("Pass")
                
        if "Fail" not in self.lst_status:
            self.logger.info("***** Login DDT test passed *****")
            self.driver.close()
            self.logger.info("***** Closing Browser *****")
            assert True
        
        else:
            self.logger.info("***** Login DDT test failed *****")
            self.logger.info("***** Closing Browser *****")
            self.driver.close()
            assert False
            
        self.logger.info("*********** Completed TEST_002_Login_DDT ***********")
        self.logger.info("***** End of TEST_002_Login_DDT *****")
                
            
            
        
            
            
        
        
        
    
    