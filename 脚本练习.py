#/usr/bin/python
#-*-coding:utf-8-*-

#选择法排序
# a=[2,4,1,5,8,6]
# b=len(a)
# for i in range (b):
#     for j in range(i+1,b):
#        if a[i]>a[j]:
#            a[i],a[j]=a[j],a[i]
# print(a)
# #冒泡法排序
# a=[2,4,1,5,8,6]
# b=len(a)
# for i in range(b):
#     for j in range( b-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)
# #质数之和（100以内）
# d=0
# for i in range(2,100):
#     for j in range (2,100):
#         c=i%j
#         if c==0:
#             break
#     if i==j:
#         d=d+i
# print(d)
# #水仙花数
# for i in range (100,1000):
#     q=i//100
#     w=i//10%10
#     e=i%10
#     if i==q**3+w**3+e**3:
#         print(i)
#阶乘之和（任意输入）
# a= int((input('输入任意一个正整数字：'))
# if float(a)>=0:
#     print('无阶乘')
# elif int(a)>=1:
#     print('有阶乘')
# q=0
# for w in range (1,a+1):
#     c=1
#     for t in range (1,w+1):
#         c=c*t
#         q=q+c
# print('阶乘之和为：{}'.format(q))
# import random
# q=('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
# c=[ ]
# for i in range (6):
#     b=random.randint(0,61)
#     r=''.split(q)
#     c.append(q[b])
#     v=''.join(c)
# print(v)
# e=input('输入验证码：')
# if len(e)==6:
#     if v==e:
#         print('你不是瞎子')
#     else :
#         print('看不清')
# else:
#     print('验证码不符合规则')
#
# a='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# c=[]
# while 1:
#     for i in range(6):
#         import random
#         b=random.randint(0,len(a)-1)
#         e=c.append(a[b])
#     e=''.join(c)
#     print(e)
#     d=input('请输入验证码:')
#     if len(d)==6:
#         if d==e:
#             print('验证成功!')
#             break
#         else:
#             print('验证失败!')
#     else:
#         print('长度不够6位，验证失败!')
#     c.clear()
#     f=input('还要继续输入验证码吗?(Y/N)')
#     if f=='Y':
# continue
# elif f=='N':
#     print('那好吧,下次再见!')
#     break
# else:
#     g=input('输入错误,只能输入"Y"或"N"!再次确认还要继续吗?')
#     if g=='Y':
#         continue
#     elif g=='N':
#         print('那好吧,下次再见!')
#         break
#          else:
#             print('很抱歉,您又输错了!再见!')
#             break
# a=[1,3,4,7]
# b=1
# for i in range (b):
#     a.insert(len(a),a[0])
#     a.remove(a[0])
#     print(a)
# a=input('请输入一个正整数:')
# b=0
# for i in range(1,int(a)):
#     c=1
#     for j in range (1,i+1):
#         c=c*j
#     b=b+c
# print(b)
# a= int (input('输入任意一个正整数字：'))
# q=0
# for w in range (1,a+1):
#      c=1
#      for t in range (1,w+1):
#          c=c*t
#      q=q+c
# print('阶乘之和为：{}'.format(q))
# import pymysql
# d = pymysql.connect(
#         host = '192.168.2.183',
#         port = 3306,
#         user = "root",
#         password = "123456",
#         charset = "utf8",
#         database = 'hao123'
#     )
# a = d.cursor()
# sql="""create table kebiao(ID int ,name char(20),) """
# try:
# data=a.execute(sql)
# print(data)
# class Book(object):
#
#         def __init__(self, name, author, status, bookindex):
#                 self.name = name
#                 self.author = author
#                 self.status = status
#                 self.bookindex = bookindex
#
#         def __str__(self): #魔法方法的一种，自动将对象的属性
#                 if self.status == 1:
#                         stats = '未借出'
#                 elif self.status == 0:
#                         stats = '已借出'
#                 else:
#                         stats = '状态异常'
#                 return '书名: 《%s》 作者: %s 状态: <%s> 位置: %s' \
#                        % (self.name, self.author, stats, self.bookindex)
#
#
# class BookManage(object):
#         books = []
#
#         def start(self):
#                 self.books.append(Book('python', 'guido', 1, 'ISO9001'))
#                 self.books.append(Book('c', '谭浩强', 1, 'NFS8102'))
#                 self.books.append(Book('java', 'westos', 1, 'PKA7844'))
#                 # 0:借出 1：存在
#                 # python 1
#                 # c 1
#                 # java 1
#
#         def Menu(self):
#                 self.start()
#                 while True:
#                         print("""
#       图书管理系统
#   1.查询图书
#   2.增加图书
#   3.借阅图书
#   4.归还图书
#   5.退出系统
#   """)
#
#                         choice = input('请选择：')
#
#                         if choice == '1':
#                                 self.showAllBook()
#                         elif choice == '2':
#                                 self.addBook()
#                         elif choice == '3':
#                                 self.borrowBook()
#                         elif choice == '4':
#                                 self.returnBook()
#                         elif choice == '5':
#                                 print('欢迎下次使用...')
#                                 exit()
#                         else:
#                                 print('请输入正确选择')
#                                 continue
#
#         def showAllBook(self):
#                 for book in self.books:
#                         print(book)
#
#         def addBook(self):
#                 name = input('图书名称:')
#                 self.books.append(Book(name, input('作者:'), 1, input('存储位置:')))
#                 print('图书《%s》增加成功' % name)
#
#         def checkBook(self, name):
#                 for book in self.books:
#                         if book.name == name:
#                                 return book
#                 else:
#                         return None
#
#         def borrowBook(self):
#                 name = input('借阅图书名称: ')
#                 ret = self.checkBook(name)
#                 print(ret)
#
#                 if ret != None:
#                         if ret.status == 0:
#                                 print('书籍《%s》已经借出' % name)
#                         else:
#                                 ret.status = 0
#                                 print('书籍《%s》借阅成功' % name)
#                 else:
#                         print('书籍《%s》不存在' % name)
#
#         def returnBook(self):
#                 name = input('归还图书名称:')
#                 ret = self.checkBook(name)
#
#                 if ret != None:
#                         if ret.status == 0:
#                                 ret.status = 1
#                                 print('书籍《%s》归还成功' % name)
#                                 print(ret)
#                         else:
#                                 print('书籍《%s》未借出' % name)
#                 else:
#                         print('书籍《%s》不存在' % name)
#
#
# manager = BookManage()
# manager.Menu()
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# class Email(object):
#         mail_host = 'smtp.163.com'
#         mail_port = 465
#         mail_user = '13525038273@163.com'
#         mail_pass = 'wang12345'
#         sender = "13525038273@163.com"
#         receivers = ['13750712917@163.com', '15206265349@163.com']
#         def xieyoujian(self) :
#                 self.subject = "2019.8.15日报"
#                 content = "学习python—邮箱发送"
#                 self.message = MIMEText(content, 'plain', 'utf-8')
#         def fasong(self):
#                 self.message['From'] = Header(self.sender)
#                 self.message['To'] = Header(str(";".join(self.receivers)))
#                 self.message['Subject'] = Header(self.subject)
#         def lianjie(self):
#                 s = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)
#                 s.login(self.mail_user, self.mail_pass)
#                 s.sendmail(self.sender,self. receivers,self.message.as_string())
#                 print('邮件发送成功')
#                 s.close()
# k = Email()
# k.xieyoujian()
# k.fasong()
# k.lianjie()

#异常
"""
1、python语法错误，缩进、缺少:class
2、代码逻辑的问题
"""
#异常处理
"""
处理python代码中可能出现的错误、异常
"""
# try:
#         a=1 /0
# except:
#         pritn("try 语句存在错误")

#处理异常 try...except
#格式
"""
try:
    代码块1
except:
     代码块2
try  语句没有错误时，不执行except语句，
try  语句存在错误时，执行except语句，    
except 执行异常的类型:
except 不写捕获类型时默认所有类型，指定类型后只捕获指定的类型             
"""
#指定错误类型
# try:
#         a=1 /0
#         print(name)
# except:(ZeroDivisionError,NameError):
#         pritn("try 语句存在错误")

#try ...except...finally
#try 语句存在错误，except、finally语句都被执行
#try语句不存在错误，finally语句都被执行

# try:
#         a=1/0
# except:
#         print("try语句内有bug")
# finally:
#         print("finally语句被执行了")
#try ...except...else
#当try语句存在错误，执行except，不执行else语句
#当try语句不存在错误，执行else
# try:
#         a=1/0
# except:
#         print("try语句内有bug")
# else:
#         print("else语句被执行了")
# #九九乘法表
# for i in range(1,10):
#         for j in range(1,i+1):
#                 print('{}*{}={}\t'.format(i,j,i*j), end='')
# user_1=pymysql.connect(
#         host='192.168.10.60',
#         port=3306,
#         user='root',
#         password='123456',
#         charset='utf8',
#         database='hao123'
# )
# d=user_1.cursor()
# sql1='create table  xinxibiao (ID int,name char(20),chengji int)'
# e=d.execute(sql1)
# # print(d.fetchall())
# c=xlrd.open_workbook(filename='信息表.xlsx')
# table=c.sheets()[0]
# k=table.nrows
# x=[]
# for i in range(k):
#         a=table.row_values(i)
#         # print(a)
#         # g=str(a)
#         x.append(a)
# for j in  x:
#         sql2 ='insert into  xinxibiao values(%s,%s,%s)'
#         e=d.execute(sql2,(j[0],j[1],j[2]))
#         print(e)


#将Excel数据写入数据库中

# c=xlrd.open_workbook(filename='信息表.xlsx')
# table=c.sheets()[0]
# k=table.nrows
# x=[]
# for i in range(k):
#         a=table.row_values(i)
#         k=tuple(a)
#         # print(k)
#         x.append(k)
#         j=tuple(x)
# print(j)
# user_1 = pymysql.connect(
#                 host='192.168.10.109',
#                 port=3306,
#                 user='root',
#                 password='123456',
#                 charset='utf8',
#  )
# d = user_1.cursor()
# sql0='create database xinxibiao22  charset="utf8"'
# sql1='use xinxibiao22'
# sql2 = 'create table  xinxibiao44(ID int,name char(20),chengji int) charset="utf8"'
# e = d.execute(sql0),d.execute(sql1),d.execute(sql2)

# for k in j:
#     print(k)
   # sql3=f"insert into xinxibiao22.xinxibiao33 values {k}"
   # e=d.execute(sql3)
    # print(e)
#将数据库数据写入Excel表格中
# user_1 = pymysql.connect(
#                  host='192.168.10.109',
#                  port=3306,
#                  user='root',
#                  password='123456',
#                  charset='utf8',
#                  database='xinxibiao22'
#   )
# d = user_1.cursor()
# sql1='select * from  xinxibiao33;'
# k=d.execute(sql1)
# a=d.fetchall()
# x=[]
# for i in a:
#     s=list(i)
#     x.append(s)
# # print(x)
# d =xlwt.Workbook()
# table =d.add_sheet("表一")
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         table.write( i,j,x[i][j])
# d.save('vvv.xls')
import requests
import     re
# user_1 = pymysql.connect(
#                   host='192.168.10.109',
#                   port=3306,
#                   user='root',
#                   password='123456',
#                   charset='utf8',
#    )
# d = user_1.cursor()
# x=[]
# k=[]
# # j=[]
# r=requests.get(url='https://www.fpzw.com/xiaoshuo/109/109813/')
# data=r.content.decode(encoding='gbk')
# # print(data)
# a=re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
# b=re.findall(a,data)
# # print(b)
# for i in range(10):
#         print(b[i])
        # k.append(b[i][1])
# print(k)
#  c=b[i][1]
#  q = c.split(',')
#  j.append(tuple(q))
#  for n in (tuple(j)):
#          r = requests.get(url=f'https://www.fpzw.com/xiaoshuo/109/109813/{b[i][0]}')
#          baba=r.content.decode(encoding='gbk')
#          a=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
#          g=re.findall(a,baba)
#  for  m   in g:
#         x.append(m)
#         sql1='create database xiaoshuo charset="utf8"'
#         sql2='use xiaoshuo'
#         sql3='create table  xiaoshuo1(章节 text,内容 text )charset="utf8"'
#  # for j in z:
#  #      print(j)
#         sql4=f"insert into xiaoshu.xiaoshuo1('章节')values{n}"
# # for a in x:
# #         print(a)
# #         sql5 = f"insert into xiaoshu.xiaoshuo1('内容')values{a}"
# e = d.execute(sql1), d.execute(sql2), d.execute(sql3),d.execute(sql4)







# x.append(b)
# k=re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
# b=re.findall(k,data)
# x.append(b)
# print(x)


