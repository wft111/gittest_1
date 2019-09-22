#/usr/bin/python
#-*-coding:utf-8-*-
#flask web 框架
"""
1、django
2、flask
3、bottle
4、tormdon
"""
#web页面一般分两种
"""
1、静态的，页面不会发生变动
2、动态的，页面数据时时刷新的
"""
#flask  --->python开发web网页，数据交互的一个web框架
from  flask import Flask
app =Flask(__name__)
@app.route('/')
def hello():
    return "hello ,falsk"
if __name__=='__main__':
    app.run(host='127.0.0.1',port=6000)