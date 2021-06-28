# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm

import time
import pytesseract
from PIL import Image, ImageEnhance
from selenium import webdriver

url = "http://172.31.236.33/"
# 1、打开浏览器，最大化浏览器
driver = webdriver.Chrome()
driver.get(url)
#driver.implicitly_wait(10)#隐式等待10s
driver.maximize_window()#最大化窗口
time.sleep(4)
username = driver.find_element_by_xpath('//*[@id="userName"]')
possword = driver.find_element_by_id('password')
code1 = driver.find_element_by_id('verifyCode')
#定位图片位置
codess = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div[3]/div/div/span/div/div[2]/button')
driver.save_screenshot('D://test//01.png')#保存到本地
ran = Image.open("D://test//01.png")#打开截图，获取验证码位置，截取保存验证码
box = (1062, 441, 1234, 503) # 获取验证码位置，手动定位，代表（左，上，右，下）
ran.crop(box).save("D://test//02.png")#把获取的验证码保存
#获取验证码图片，读取验证码
imageCode = Image.open("D://test//02.png") #打开保存的验证码图片
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.load() # 对比度增强
sharp_img.save("D://test//03.png")#保存图像增强，二值化之后的验证码图片
time.sleep(2)
print(sharp_img)#打印图片的信息
code = pytesseract.image_to_string(sharp_img).strip()#读取验证码
print('验证码识别为：'+str(code))#输出验证码
username.send_keys('root')
possword.send_keys('root123')
code1.send_keys(code)
denglu= driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div[4]/div/div/span/button').click()