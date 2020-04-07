from common.read_yaml import ReadYaml
from common.base import Base
import time
import os

#设置页
class SettingPage(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        yaml = ReadYaml("./data/element_loc.yaml")
        self.setting_btn_loc=yaml.analysis_data("index","setting_btn_loc") # 【设置】按钮

    def enter_in_setting_page(self):
        '''进入设置页'''
        self.click(self.setting_btn_loc)

    def check_setting_btn_exist(self):
        '''检查【设置】按钮是否存在'''
        return self.is_element_exist(self.setting_btn_loc)
