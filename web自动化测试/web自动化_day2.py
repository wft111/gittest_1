#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author  : WFT

# @Time    : 2019/9/11 9:20

# @Software: PyCharm

# @FileName: web自动化_day2.py
"""
from time import sleep
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
dr = webdriver.Chrome()
dr.get('http://www.jd.com')
sleep(4)
dr.maximize_window()
# sleep(2)
# dr.find_element_by_xpath('/html/body/button').click()
sleep(2)
"""
'''
# 处理弹出框

# 切换到弹出框
ww = dr.switch_to_alert()
# 获取弹出框的文本
print(ww.text)
sleep(2)
# 输入数据
ww.send_keys('张三')
# 点击弹出框上面的确定
sleep(5)
ww.accept()
# 点击取消
# ww.dismiss()
'''
# 9、控制浏览器的滚动条
'''
javascript 中对应的滚动条的语句：arguments[0].scrollIntoView() 
滚动到指定的位置
'''
# dd =dr.find_element_by_xpath('//*[@id="J_channels"]/div/div[2]/div/div/div[2]/div/div[12]/a/span[1]')
# sleep(3)
# 执行JavaScript语句
# dr.execute_script('arguments[0].scrollIntoView();',dd)


# 控制浏览器滚动条，根据距离滚动
# for i in range(0,1000,200):
#     js = f"var q=document.documentElement.scrollTop={i}"
#     dr.execute_script(js)
#     sleep(3)

'''
# 模拟鼠标的操作操作
from selenium.webdriver.common.action_chains import ActionChains
for i in range(1,19):
       kk = dr.find_element_by_xpath(f'//*[@id="J_cate"]/ul/li[{i}]').find_elements_by_class_name('cate_menu_lk')
# dd = dr.find_element_by_xpath('//*[@id="J_cate"]/ul/li[14]/a[3]')
       for j in kk:
            sleep(2)
# 将鼠标移动到元素中心点
# 动作链--->ActionChains(dr).move_to_element(dd)  执行动作---->.perform()
            ActionChains(dr).move_to_element(j).perform()
'''
# QQ空间
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium import  webdriver
import  selenium.webdriver.support.ui as ui
dr=webdriver.Chrome()
dr.get('https://qzone.qq.com/')
dr.maximize_window()
sleep(2)
# 智能等待的等待器
unt=ui.WebDriverWait(dr,10)

# 设置智能等待
unt.until(lambda dr:dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]').is_displayed())

"""
dr.switch_to.frame('login_frame')
dr.find_element_by_id('switcher_plogin').click()
sleep(2)
dr.find_element_by_id('u').send_keys('3216223631')
sleep(2)
dr.find_element_by_id('p').send_keys('deqweqwq')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(3)
dr.switch_to.frame('tcaptcha_iframe')
ww = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')

"""
# drag_and_drop 拖拽从起始位置拖到目的位置
# drag_and_drop（起始，目的）
# drag_and_drop_by_offset（拖拽从起始位置拖到某个点的位置）
# drag_and_drop_by_offset（起始：x，y）
"""
ActionChains(dr).drag_and_drop_by_offset(ww,190,0).perform()
"""
