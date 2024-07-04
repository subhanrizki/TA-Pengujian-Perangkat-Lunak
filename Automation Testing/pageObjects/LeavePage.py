import time
import pytest
from selenium.webdriver.support.ui import Select

class LeavePage:
    
    link_menubarLeave_xpath = "//*[@id='menu_leave_viewLeaveModule']"
    link_applyleave_xpath = "//*[@id='menu_leave_applyLeave']"
    dropdown_leavetype_xpath = "//select[@id='applyleave_txtLeaveType']"
    textbox_fromdate_xpath = "//input[@id='applyleave_txtFromDate']"
    textbox_todate_xpath = "//input[@id='applyleave_txtToDate']"
    dropdown_duration_xpath = "//select[@id='applyleave_duration_duration']"
    textarea_leavecomment_xpath = "//textarea[@id='applyleave_txtComment']"
    button_applyleave_xpath = "//input[@id='applyBtn']"
    table_leavedate_xpath = "//*[@id='content']/div[1]/div[2]/table/tbody/tr/td[1]"
    
    def __init__(self,driver):
        self.driver = driver
    
    def clickMenuLeave(self):
        self.driver.find_element_by_xpath(self.link_menubarLeave_xpath).click()
        time.sleep(1)
    
    def clickApplyLeave(self):
        self.driver.find_element_by_xpath(self.link_applyleave_xpath).click()
        time.sleep(2)
    
    def setLeaveType(self,leavetype):
        leavetype_value = self.driver.find_element_by_xpath(self.dropdown_leavetype_xpath) 
        Select(leavetype_value).select_by_visible_text(leavetype)
        #leavetype_value.select_by_visible_text(self,leavetype)
        time.sleep(1)
    
    def setFromDate(self,fromdate):
        self.driver.find_element_by_xpath(self.textbox_fromdate_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_fromdate_xpath).send_keys(fromdate)
    
    def setToDate(self,todate):
        self.driver.find_element_by_xpath(self.textbox_todate_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_todate_xpath).send_keys(todate)
    
    def setLeaveComment(self,comment):
        self.driver.find_element_by_xpath(self.textarea_leavecomment_xpath).clear()
        self.driver.find_element_by_xpath(self.textarea_leavecomment_xpath).send_keys(comment)
    
    def clickApply(self):
        self.driver.find_element_by_xpath(self.button_applyleave_xpath).click()
        
    def getLeaveStatusMessage(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_applyleave_xpath).click()
        time.sleep(1)
        status = self.driver.find_element_by_xpath(self.table_leavedate_xpath).text
        return status
        