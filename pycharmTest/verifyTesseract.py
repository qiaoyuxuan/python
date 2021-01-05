# coding=utf-8   为了防止乱码问题，以及方便的在程序中添加中文注释，把编码统一成 UTF-8
# Time:2018/6/22
# Author:yuxuanqiao

from selenium import webdriver
from PIL import Image, ImageEnhance  #导入图片解析包
from pytesseract import *  # 导入验证码包
import time



# 获取验证码函数,传入driver浏览器，和验证码图片imgElement，即可返回文本验证码
def get_auth_code(driver, imgElement):
    driver.save_screenshot(u"截取验证码/verifyCode.png")  # 获取验证码的方法，截取当前网页，该网页有我们需要的验证码
    time.sleep(2)
    size = imgElement.size  # 获取验证码的大小
    location = imgElement.location  # 获取验证码x,y轴坐标
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))  # 计算验证码整体坐标
    i = Image.open(u"截取验证码/verifyCode.png") # 打开截图
    imgry = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
    imgry.save(u"截取验证码/getVerifyCode.png")
    im = Image.open(u"截取验证码/getVerifyCode.png")
    im = im.convert('L')  # 图像加强，二值化
    sharpness = ImageEnhance.Contrast(im)  # 对比度增强
    sharp_img = sharpness.enhance(2.0)
    sharp_img.save(u"截取验证码/newVerifyCode.png")
    newVerify = Image.open(u"截取验证码/newVerifyCode.png")
    text = image_to_string(newVerify).strip()  # 使用image_to_string识别验证码，需要安装配置tesseract
    return text

# 批量注释：Ctrl+/
# if __name__ == '__main__':
#
#     driver = webdriver.Chrome()
#     driver.get('http://jingangtest.yto56.com.cn/stationwebexp/logout')
#     # driver.maximize_window()
#     imgElement = driver.find_element_by_xpath(".//*[@id='vildateImg']")  # 定位验证码
#     authCodeText = get_auth_code(driver, imgElement)
#     # pandarola_login(driver, 'admin', '1', authCodeText)
#     driver.quit()

