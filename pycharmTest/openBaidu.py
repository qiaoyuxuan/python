# coding=utf-8   为了防止乱码问题，以及方便的在程序中添加中文注释，把编码统一成 UTF-8
import time
from selenium import webdriver                              # 导入selenium的webdriver包,以使用webdriverAPI进行自动化脚本

driver = webdriver.Chrome()                                 # 将控制的 webdriver 的Chrome赋值给 driver
# driver.maximize_window()                                  # 浏览器窗口最大化
driver.set_window_size(960,660)                             # 设置浏览器窗口大小

first_url = 'http://www.baidu.com'
driver.get(first_url)
time.sleep(3)                                               # 等待3秒刷新页面
print("access to %s " % first_url)                          # 打印百度地址，通过%s引用字符串变量
driver.find_element_by_id("kw").send_keys("hello world")    # 通过 id=kw 定位到百度的输入框，输入 hello world
driver.find_element_by_id("su").click()                     # 通过 id=su 定位的搜索按钮，并向按钮发送单击事件click()
time.sleep(2)
driver.get_screenshot_as_file("D:\A.jpg")                   # 截图（仅浏览器部分）
driver.back()                                               # 返回上一页
time.sleep(2)
driver.forward()                                            # 跳转到下一页
# driver.quit()                                             # 用于结束进程，关闭所有窗口（在结束测试的时候使用，可回收C盘临时文件）
# driver.close()                                            # 仅用于关闭当前窗口

