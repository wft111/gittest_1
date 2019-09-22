#/usr/bin/python
#-*-coding:utf-8-*-
#面向对象的特点？
"""
1、封装
      封装指的是：对数据和代码逻辑的处理
2、继承
      继承的分类：
      单继承：B类继承A类；只继承一类
      多继承：B类继承A类、同时又继承C类；同时继承多个类
3、多态
"""
#定义一个A类
# class A (object):
#     #类属性
#     name = 'abc'
#     age = 18
#     def __init__(self,a):
#         #对象属性
#         self.a = a
#         #实例方法
#     def b(self):
#         print("这是A类的实例方法b")
#
#
# #定义一个B类
# class B (A):
#     def c (self):
#         priself.b()
# # #子类拥有父类的全部属性、方法
# # #创建一个B类的对象
# # b = B('hello')
# # #子类能不能使用父类的属性、方法？
# # print(b.name)
# # print(b.a)
# # b.b()
# # b.c()nt(f"父类的类属性有name：{self.name}，age:{self.age}")
        #在B类里直接使用A类的方法
#

"""
面向对象——多态
1、子类的方法与父类的方法名一致
2、如果想使用父类的方法：
       在子类中定义一个方法
       在函数里写super（）.父类的方法名字
3、子类对象在使用父类方法的，只需要通过对象.子类中定义的方法名       
"""
# class C (object):
#     def foo(self):
#         print("这是C类的实例方法")
# class D(C):
#     def foo (self):
#         print('这是D类的实例方法')
# #super()类
#     def K(self):
#         super().foo()
#
# d1 =D()
# #使用d类里的实例方法
# d1.foo()
#
# #d2使用c类的实例方法
# d2=D()
# d2.K()


import pymysql,re,requests
class Book (object):
    def __init__(self,url,encoding,r1,r2,host,user,password,database):
        self.url=url
        self.encoding=encoding
        self.r1=r1
        self.r2=r2
        self.host=host
        self.user=user
        self.password=password
        self.database=database
    def neirong(self):
        self.x=[ ]
        s=requests.get(url=self.url)
        self.d=s.content.decode(encoding=self.encoding)
        r1=re.compile(self.r1)
        h=re.findall(r1,self.d)
        self.x.append(tuple(h))
        r2=re.compile(self.r2)
        k=re.findall(r2,self.d)
        self.x.append(tuple(k))
        self.g=tuple(self.x)    #转变成元组格式

    def lianjie(self):
        d=pymysql.connect(
            host=self.host,
            port=3306,
            user=self.user,
            password=self.password,
            charset='utf8',
            database=self.database
            )
        self.q=d.cursor()
        sql1='create table xiaoshuo(章节 text,内容 text)charset="utf8"'
        for i in self.g:
            sql2=f"insert into xinxibiao22.xiaoshuo{i}"
            e=self.q.execute(sql1),self.q.execute(sql2)
A=Book('https://www.fpzw.com/xiaoshuo/87/87590/17125664.html','gbk',r'<h2>(.*?)</h2>',r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />','192.168.10.109','root','123456',"xinxibiao22")
A.neirong()
A.lianjie()


