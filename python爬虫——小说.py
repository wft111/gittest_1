#/usr/bin/python
#-*-coding:utf-8-*-

# 爬虫框架   scrapy
"""
爬虫：通过python代码获取网络存放的数据资源 【文件、图片、mp3】
反爬虫：防止资源被爬虫代码获取
反爬机制：属于反爬虫的技术手段之一
最常见的反爬机制：
1、封IP地址
2、封物理网卡的mac地址
3、验证码
4、服务器传输给浏览器的数据通过异步加载。
"""
"""
re模块
requests python发送http/https请求  ，接受响应数据的一个第三方库
"""
import  re
import requests
"""
User-Agent:代表浏览器
"""
import pymysql,re,requests
x ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#get请求  获取资源
#第一步：发送请求
r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/17125664.html', headers=x)
#第二步：获取响应的结果、数据
"""
content获取请求之后的响应数据
"""
x=[]
data=r.content.decode(encoding='gbk')
# print(data)
a=re.compile(r'<h2>(.*?)</h2>')
b=re.findall(a,data)
x.append((b))
# print(x)
c=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
f=re.findall(c,data)
k=','.join(f)
s=k.split(' ')
x.append(s)
k=tuple(x)
# print(k)
# for i in k:
#        print(i)
user_1 = pymysql.connect(
                  host='192.168.10.109',
                  port=3306,
                  user='root',
                  password='123456',
                  charset='utf8',
                  database='xinxibiao22'
   )
d = user_1.cursor()
sql1='create table xiaoshuo10(章节 text,内容 text)charset="utf8"'
for i in k:
      # print(i)
    sql2 = "insert into xiaoshuo10 values(%s,%s) (i[1],i[2])"
    e = d.execute(sql1), d.execute(sql2)




#"<h2>(.*?)</h2>" ctrl +  f  搜索
# k=open(file='b.txt',mode='w',encoding='utf-8')
# for i in f:
#     print(k.write(f'{i}\n'))
# r=requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=x)
# d = r.content.decode(encoding='gbk')
# c=re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
# f=re.findall(c,d)
# # print(f)
# k = open(file='a.txt', mode='a', encoding='utf-8')
# for i in f:
#       # print(i)
#     s= requests.get(url=f'https://www.fpzw.com/xiaoshuo/87/87590/{i[0]}',headers=x)
#     m = s.content.decode(encoding='gbk')
#     r1 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
#     h = re.findall(r1, m)
#     # print(f'{h}\n')
#     k = open(file='a.txt', mode='a', encoding='utf-8')
#     for g  in i:
#           print(k.write(f'{g[1]}'))
#     for j in h:
#           print(k.write(f'{j}\n'))




