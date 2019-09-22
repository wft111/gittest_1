#!/usr/bin/python
# -*- coding: utf-8 -*-

# @Author  : WFT

# @Time    : 2019/8/21 9:09

# @Software: PyCharm

# @FileName: web自动化测试工具.py

# 导入selenium中的webdriver模块

# import  time
# from selenium import webdriver
# 打开的浏览器， dr相当于鼠标
# dr = webdriver.Chrome()
# 在地址栏中输入网址并请求
# dr.get('http://ifeng.com')

# 获取标题 //  dr.title
# 断言：将实际结果跟预期结果作对比 assert
# assert dr.title == '百度一下，你就知道'
# 获取网址
# print(dr.current_url)

# time.sleep(3)
# dr.get('https://www.ifeng.com')
# time.sleep(3)
# 退回到上一个页面
# dr.back()
# time.sleep(3)
# 前进到下一个页面
# dr.forward()
# 页面最大化
# dr.maximize_window()
# 页面最小化
# dr.minimize_window()
# 设置窗口大小
# dr.set_window_size(500,500)
# 设置浏览器窗口的位置
# dr.set_window_position(500,500)

# selenium的核心：定位
# 提供的定位方法有8种：

# 1、id定位 唯一的
# 动作：点击click(),输入send_keys(内容)
# ww=dr.find_element_by_id('kw')
# kk=ww.send_keys('python')
# time.sleep(3)
# dr.find_element_by_id('su').click()

# 2、class定位
# ww=dr.find_element_by_class_name('s_ipt')
# kk=ww.send_keys('python')
# time.sleep(3)
# dr.find_element_by_id('su').click()

# 3、name定位
# ww=dr.find_element_by_name('wd')
# kk=ww.send_keys('python')
# time.sleep(3)
# dr.find_element_by_id('su').click()

# 4、Link_text 定位 通过文本定位 唯一
# kk=dr.find_element_by_link_text('新闻')
# kk.click()

# 5、partial_Link_text 模糊文本定位
# dr.find_element_by_partial_link_text('视').click()

# 6、tag_name  标签定位  不是唯一的
# dr.find_element_by_tag_name('')

# 7、xpath 路径定位 xpath是一种语言：路径标记语言 ——>绝对路径，相对路径
# ww=dr.find_element_by_xpath('//*[@id="kw"]')
# kk=ww.send_keys('python')
# time.sleep(3)
# dr.find_element_by_xpath('//*[@id="su"]').click()

# 8、css_selector  通过css定位
# dr.find_element_by_css_selector()

# 切换框架，只能是id的值和name的值
# dr.switch_to.frame('id值/name值')   -->iframe:内嵌框架
# 或者是定位到具体框架位置再切换 例如：ww=dr.find_element_by_xpath('//*[@id="su"]')   dr.switch_to.frame(ww)
# 退出框架 （退出到最开始的第一层框架）
# dr.switch_to.default_content()
# 退出到上一层框架
# dr.switch_to.parent_frame()

# 获取当前窗口的句柄
# print(dr.current_window_handle)

# 获取所有窗口的句柄 ，，，列表
# print(dr.current_window_handles)   qq = dr.window_handles  #获取所有句柄
# ww =dr.current_window_handles

# 切换窗口 只能通过句柄来切换
# dr.switch_to.window(ww[索引值])

######################################
# 定位一组元素:一次性定位到多个某些属性相同的元素
# 层级定位:先定位到大的范围，再从大的范围里定位元素
# ww=dr.find_element_by_id('searchHotelLevelSelect').find_elements_by_tag_name('option')
# for i in ww:
#     i.click()
#     time.sleep(2)
'''
获取京东菜单
for i in range(1,19):
       kk = dr.find_element_by_xpath(f'//*[@id="J_cate"]/ul/li[{i}]').find_elements_by_class_name('cate_menu_lk')
       for j in kk:
           print(j.text)
'''
# ss = dr.find_element_by_id('nav').find_elements_by_tag_name('li')
# for i in ss:
#     i.click()
# 关闭浏览器
# time.sleep(3)
# dr.quit()


# # 登录QQ邮箱并发送QQ邮箱
'''
from time import sleep
from selenium import  webdriver
dr = webdriver.Chrome()
dr.get('http://mail.qq.com')
dr.maximize_window()
sleep(2)
dr.switch_to.frame('login_frame')      # 进入内嵌的输入框
dr.find_element_by_id('switcher_plogin').click()     # 点击输入账号密码输入
dr.find_element_by_id('u').send_keys('1761295435')    # 账号
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('password') # 密码
dr.find_element_by_xpath('//*[@id="login_button"]').click()  # 点击登录
sleep(3)
dr.find_element_by_xpath('//*[@id="composebtn"]').click()  # 点击写信
dr.switch_to.frame('mainFrame')   # 进入内嵌框架--->收件人
sleep(2)
dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('1148389400@qq.com')  # 定位到收件人并且输入账号
sleep(2)
dr.find_element_by_id('subject').send_keys('web自动化测试学习')  # 输入邮件主题
sleep(1)
dr.switch_to.frame(dr.find_element_by_class_name('qmEditorIfrmEditArea'))  # 定位进入输入文本框架
sleep(2)
dr.find_element_by_xpath('/html/body').send_keys('如何使用selenium自动化测试') # 写入文本
dr.switch_to.parent_frame()  # 退出文本内嵌框架
dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()  # 点击发送
sleep(3)
dr.switch_to.parent_frame()  # 退出第一层框架
sleep(2)
dr.find_element_by_xpath('//*[@id="SetInfo"]/div[1]/a[3]').click()  # 点击退出账号
sleep(10)
dr.quit()  #关闭浏览器
'''
# 自动登录QQ空间并发送说说
'''
from time import sleep
from selenium import  webdriver
dr=webdriver.Chrome()
dr.get('https://qzone.qq.com/')
dr.maximize_window()
sleep(2)
dr.switch_to.frame('login_frame')
dr.find_element_by_id('switcher_plogin').click()
sleep(2)
dr.find_element_by_id('u').send_keys('393808764')
sleep(2)
dr.find_element_by_id('p').send_keys('password')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
kk= dr.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys('web自动化测试')
sleep(2)
dr.find_element_by_xpath('//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]/span').click()
'''

'''
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get('https://music.163.com/')
dr.maximize_window()
dr.find_element_by_xpath('//*[@id="g-topbar"]/div[1]/div/ul/li[2]/span/a/em').click()
sleep(2)
dr.switch_to.frame(dr.find_element_by_xpath('//*[@id="g_iframe"]'))
sleep(2)
dr.find_element_by_xpath('/html/body/div[3]/div/div/a').click()
sleep(2)
dr.switch_to.default_content()
dr.switch_to.frame(dr.find_element_by_xpath('//*[@id="auto-id-cJ5eAMneroaB3EEh"]'))
sleep(2)
dr.find_element_by_xpath('//*[@id="auto-id-C9QWCl8v5Rts8Je2"]/div/div[1]/div[2]/a/i').click()
'''

