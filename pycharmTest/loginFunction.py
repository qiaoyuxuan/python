# coding=utf-8   为了防止乱码问题，以及方便的在程序中添加中文注释，把编码统一成 UTF-8
# Time:2018/6/22
# Author:yuxuanqiao

import verifyTesseract
import time
from selenium import webdriver

# 登录函数，参数：浏览器、用户名、密码、验证码
def logging(driver, logginName, pwd, verifyCode):
    driver.find_element_by_name("username").send_keys(logginName)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_xpath(".//*[@id='rand']").send_keys(verifyCode)
    driver.find_element_by_id("submitlogin").click()
    time.sleep(2)

    try:
        driver.find_element_by_xpath("html/body/div[1]/div[2]/div[1]/ol/li/a").is_displayed()
    except:
        # print("登录失败")
        title = "登录失败"
    else:
        title = driver.find_element_by_xpath("html/body/div[1]/div[2]/div[1]/ol/li/a").text
        assert title == u"首页"
        # print(title)
    return title



