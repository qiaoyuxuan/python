# conding=utf-8
# Time:2018/6/25
# Author:yuxuanqiao

from selenium import webdriver
import loginFunction
import verifyTesseract

# 妈妈驿站前台登录，调用verifyTesseract解析并获得验证码数字，再调用loginFunction登录
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://jingangtest.yto56.com.cn/stationwebexp/logout')
    imgElement = driver.find_element_by_xpath(".//*[@id='vildateImg']")
    authCodeText = verifyTesseract.get_auth_code(driver, imgElement)
    print(authCodeText)
    title = loginFunction.logging(driver, '13661685161', '1234056', authCodeText)
    print(title)
    driver.quit()
