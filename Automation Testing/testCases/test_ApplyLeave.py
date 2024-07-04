import pytest
from pageObjects.LeavePage import LeavePage
from pageObjects.LoginPage import LoginPage
from testCases.conftest import setup
from utilities.readProperties import ReadConfig

class Test_003_ApplyLeave:
    
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUser()
    password = ReadConfig.getPass()
    
    def test_ApplyLeave(self,setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        
        self.leavepage = LeavePage(self.driver)
        self.leavepage.clickMenuLeave()
        self.leavepage.clickApplyLeave()
        
        self.leavepage.setLeaveType("Vacation US")
        self.leavepage.setFromDate("2020-09-10")
        self.leavepage.setToDate("2020-09-10")
        self.leavepage.setLeaveComment("Not Keeping Well")
        self.leavepage.clickApply()
        
        status = self.leavepage.getLeaveStatusMessage()
        
        if status == "2020-09-10":
            print("Leave Applied Successfully for Date :" + "2020-09-10")
            assert True
            self.driver.close()
        else:
            print("Some Error Occurred, Please Try Again")
            assert False
            self.driver.close()