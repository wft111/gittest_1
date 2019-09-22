#!/usr/bin/python
#-*-coding:utf-8-*-
# import re
# import requests
# q=requests.get(url='http://www.doutula.com/photo/list/?page=31')
# d=q.content.decode(encoding='utf-8')
# # print(d)
# r1=re.compile(r'data-original="(.*?)" alt="(.*?)"' )
# data=re.findall(r1,d)
# # print(data)
# for i in data:
#     urls=[]
#     urls.append(i[0])
#     # print(urls)
#     for j in urls:
#          req = requests.get(url=f'{j}')
#          jiegou = req.content
#          f = open(file=f'C:/Users/123456/Desktop/表情包/{i[1]}.gif', mode='wb')
#          f.write(jiegou)
#          print(f'{i[1]}.gif')
#九九乘法表
# for i in range(1,10):
#      for j in range (1,i+1):
# 	      print('{}*{}={}\t'.format(j,i,i*j),end=' ')
#      print()
#选择法排序
# a=[2,3,4,1,6,5,8,7,0]
# b=len(a)
# for i in range(b):
#      for j in range(i+1,b):
#          if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
# a = [2, 3, 4, 1, 6, 5, 8, 7, 0]
# b = len(a)
# for i in range(b):
#     for j in range(b - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)
#质数之和
# a=0
# for i in range(2,100):
#     for j in range(2,100):
#         c=i%j
#         if c==0:
#             break
#     if i==j:
#         a+=i
# print(a)
#水仙花数
# for i in range (100,1000):
#       a=i//100
#       b=i//10%10
#       c=i%10
#       if i==a**3+b**3+c**3:
#         print(i)

# a=0
# for i in range (1,6):
#     b=1
#     for j in range (1,i+1):
#           b*=j
#     a+=b
# print(a)


#视频
# import re
# import requests
# q=requests.get(url='https://www.51miz.com/shipin/0-1-0-1.html?utm_term=1349533&utm_source=baidu')
# d=q.content.decode(encoding='utf-8')
# # print(d)
# r1=re.compile(r'280" src="(.*?).mp4"' )
# data=re.findall(r1,d)
# # print(data)
# for i in data:
#      urls=[]
#      urls.append('https:'+i+'.mp4')
#      # print(urls)
#      for j in urls:
#        # print(j)
#           req = requests.get(url=f'{j}')
#           jiegou = req.content
#           n=1,3,4,5
#           f = open(file=f'C:/Users/123456/Desktop/视频/{n}.mp4', mode='wb')
#           f.write(jiegou)


# import requests
# import  re
# q=requests.get(url='https://movie.douban.com/top250?start=25&filter=')
# d=q.content.decode(encoding='utf-8')
# # print(d)
# # r1=re.compile( '<span class="other">&nbsp;/&nbsp;(.*?)  /  (.*?)</span>')
# r2=re.compile(u'.*?<p class="">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)</p>')
# data=re.findall(r2,d)
# print(data)



from selenium import webdriver
dr =webdriver.Chrome()
dr.get('https://www.baidu.com')