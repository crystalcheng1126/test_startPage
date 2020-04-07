import pytest
from page.home_page import *
from page.setting_page import  SettingPage
import time

'''测试设置页'''
class TestSetting():
    def enter_in_start_page(self,driver,host,pkUser,pkCompany):
        '''进入起始页首页'''
        HomePage(driver).open(host,pkUser,pkCompany)
        setting=SettingPage(driver)
        return  setting

    def test_have_setting_perssion(self,host,driver):
        '''测试有管理公司-全公司&管理起始页权限，显示【设置】按钮'''
        setting = self.enter_in_start_page(driver, host, "d43c2133-a058-487d-b271-ade608548bfb",
                                            "68dc0e06-82b7-4024-9a5b-ae921cc53914")
        assert setting.check_setting_btn_exist()==True

    def test_not_have_setting_perssion(self, host, driver):
        '''测试无管理公司-全公司&管理起始页权限，不显示【设置】按钮'''
        setting = self.enter_in_start_page(driver, host, "a01ef2d3-e87f-4910-9c37-288a3dca325e","68dc0e06-82b7-4024-9a5b-ae921cc53914")
        assert setting.check_setting_btn_exist() == False



