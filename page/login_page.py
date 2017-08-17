#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-15 10:09:45
# @Author  : ditto (969956574@qq.com)
# @Link    : https://github.com/dittoyy
# @Version : $Id$
from common.base import BasePage
from selenium import webdriver

login_url = "https://passport.cnblogs.com/user/signin"

class LoginPage(BasePage):
    user_loc = ("id", "input1")
    psw_loc = ("id", "input2")
    button_loc = ("id", "signin")

    tip_loc = ("id", "tip_btn")  # 获取提示语

    # 找回密码
    find_loc = ("link text", "找回")
    reset_loc = ("link text", "重置")
    remember_loc = ("id", "remember_me")
    zhuece_loc = ("link text", "立即注册")
    fankui_loc = ("link text", "反馈问题")

    def input_username(self, text):
        self.send_keys(self.user_loc, text, is_clear=False)

    def input_psw(self, text):
        self.send_keys(self.psw_loc, text,is_clear=True)

    def click_login_button(self):
        self.click(self.button_loc)

    def get_tip(self):
        t = self.get_text(self.tip_loc)
        return t

    def click_find(self):
        self.click(self.find_loc)

    def click_reset(self):
        self.click(self.reset_loc)

    def click_remember(self):
        self.click(self.remember_loc)

if __name__ == "__main__":
    login_driver = LoginPage()
    login_driver.open(login_url)
    login_driver.input_username("xxxx")
    login_driver.input_psw("xxxx")
    login_driver.click_login_button()
    t = login_driver.get_tip()
    print t













