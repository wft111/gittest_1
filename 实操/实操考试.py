#！/usr/bin/python
#-*-coding:utf-8-*-
#九九乘法表
for i in range (1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print()


#字符串数字变整数
# a=('123445')
# b=a[::-1]
# n = 0
# for i, v in enumerate(b):
#     for j in range(0, 10):
#         if v == str(j):
#             n+= j * (10 ** i)
# print(n)

#创建目录、文件、写数据、删除目录、文件
import  os
# k=os.mkdir('aaa')
# f=open(file=r'D:\PycharmProjects\untitled\123\实操\aaa\a.txt',mode='w',encoding='utf-8')
# f.write('hello,python\n 你好世界\n你好 博文')
# os.remove(r'D:\PycharmProjects\untitled\123\实操\aaa\a.txt') #删除文件
# os.rmdir('aaa')#删除目录

#连接数据库，将内容填写进去
# import pymysql
# user_1 = pymysql.connect(
#                   host='192.168.10.60',
#                   port=3306,
#                   user='root',
#                   password='123456',
#                   charset='utf8',
#                   database='xinxibiao22'
#    )
# d = user_1.cursor()
# x=[]
# f=open(file='www.txt',mode='r',encoding='GB2312')
# k=(f.readlines())
# for i in k:
#     s=i.replace('\n',' ')
#     g=s.split(',',)
#     x.append(g)
# sql3='create table  ee(qq text,ww text ,ee text,rr text)charset="utf8"'
# sql4='insert into xinxibiao22.ee value(%s,%s,%s,%s)'
# d.execute(sql3),
# d.execute(sql4,(x[0],x[1],x[2],x[3]))

# 5、统计a.txt文件中有多少行，统计时去掉单行注释的行和空行
# f=open(file='a.txt',mode='r',encoding='GB2312')
# b=f.readlines()
# b1=[]
# for i in b:
#     c=i.replace('\n','')
#     if len(c) !=0 and c[0] !='#':
#         b1.append(c)
# print(len(b1))


 #爬取嗅事百科
# import  requests
# import  re
# import  pymysql
# aa=[]
# a=pymysql.connect(
#     host='192.168.10.60',
#     port=3306,
#     user='root',
#     password='123456',
#     charset='utf8',
#     database='xinxibiao22'
#
# )
# d=a.cursor()
# s2='create table kk(`xiaoshuo` varchar(10000)) character  set utf8 '
# d.execute(s2)
# r=requests.get(url='https://www.qiushibaike.com/text/page/2/')
# k=r.content.decode(encoding='utf-8')
# a=re.compile(r'(.*?)<br/>')
# z=re.findall(a,k)
# aa.append(z)
# for  i  in  aa:
#     bb=(str(i))
#     b1='insert into  kk  values(%s)'
#     d.execute(b1,bb)

#连接Linux主机
# import paramiko
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='192.168.10.60',
#                 port=22,
#                 username='root',
#                 password='123456'
#  )
#
# stdin,stdout,stderr=client.exec_command('ls -al') #输入Linux命令
# print(stdout.read().decode())

#发送邮件
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# mail_host='smtp.163.com'
# mail_port = 465
# mail_user='13525038273@163.com'
# mail_pass='wang12345'
# sender ="13525038273@163.com"
# receivers=['18317822978@163.com']
# subject = "2019.8.18日报"
# message=MIMEMultipart()
# message['From']=Header(sender)
# message['To']=Header(str(";".join(receivers)))
# message['Subject']=Header(subject)
# with open(file='日报总结.html',mode='r',encoding='utf-8')as f:
#     content =f.read()
# p1 = MIMEText(content, 'html', 'utf-8')
# with open(file='a.txt',mode='r',encoding='GB2312')as f:
#     d=f.read()
# p2 = MIMEText(d, 'plain', 'utf-8')
# p2['Content-Type']='application/octet-stream'
# p2['Content-Disposition'] = 'attachment;filename="hello.txt"'
# with open (file='kkk.jpg',mode='rb')as f:
#     p3 = MIMEImage(f.read())
# p3['Content-Type'] = 'application/octet-stream'
# p3['Content-Disposition'] = 'attachment;filename="kkk.jpg"'
# message.attach(p1)
# message.attach(p2)
# message.attach(p3)
# s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
# s.login(mail_user,mail_pass)
# s.sendmail(sender,receivers,message.as_string())
# print('邮件发送成功')


# 将数据库数据写入Excel表格中
# import pymysql
# import xlwt
# user_1 = pymysql.connect(
#                  host='192.168.10.60',
#                   port=3306,
#                   user='root',
#                   password='123456',
#                   charset='utf8',
#                   database='xinxibiao22'
#    )
# d = user_1.cursor()
# sql1='select * from  xinxibiao33;'
# k=d.execute(sql1)
# a=d.fetchall()
# x=[]
# for i in a:
#      s=list(i)
#      x.append(s)
# # # print(x)
# d =xlwt.Workbook()
# table =d.add_sheet("表一")
# for i in range(len(x)):
#      for j in range(len(x[i])):
#           table.write( i,j,x[i][j])
# d.save('jjj.xls')


#输入一个日期，判断是否是闰年，是第几天，是星期几
s = 0
a = input("请输入：")       # 2019-8-18
b = a.split('-')
print(b)
if int(b[0]) % 400 == 0 or (int(b[0]) % 4 ==0 and int(b[0]) % 100 != 0):
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(int(b[1])- 1):
        s += day[i]
    s += int(b[2])
    a = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    c = s % 7
    print(f"{b[0]}年是闰年,是一年的第{s-1}天，今天是{a[c]}")
else:
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(int(b[1])- 1):
        s += day[i]
    s += int(b[2])
    a = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    c = s % 7
    print(f"{b[0]}年不是闰年,是一年的第{s-1}天，今天是{a[c]}")
