# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.meican.com/')
driver.set_window_size(1000,800)
driver.find_element_by_partial_link_text('用户登录').click()
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('18236344529')
driver.find_element_by_class_name('next').click()
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('Hanpeiying521')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="__layout"]/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[2]/div/div[1]/svg[2]/g').click()
