
#-*- codeing = utf-8 -*-
#@Time : 30/1/2021
#@Author : Junjie Li
#@File : hello.py
#@Software : Vscode

from flask import Flask, render_template,request #渲染文档
import jinja2
import werkzeug
import datetime

hello = Flask(__name__ ,template_folder="../templates")  # 导入框架


@hello.route('/')        #解析路由,通过用户访问的路径，匹配相近的函数
def hello_world():
    return "hello world !"


@hello.route("/index")        
def _hello():
    return "hello !"

@hello.route("/user/<name>")      #通过访问路径，获取用户字符串参数
def welcome(name):
    return "hello,%s"%name

@hello.route("/user/<int:id>")      #通过访问路径，获取用户int参数  还有可以float <float:id>
def welcome2(id):
    return "hello,%d vip "%id

#路由的路径 不能重复， 用户只能通过唯一路径进行访问

@hello.route("/css")
def css():
    return render_template("css.html")   # 返回给用户渲染后的网页文件

#向页面传递变量
@hello.route("/variable")
def variable():
    time = datetime.date.today()    # 普通变量
    name = ["俊杰","出门","无法"]     # list 
    task = {"任务":"打扫卫生","时间":"三个小时"} #字典
    return render_template("css.html", var=time, list = name, task=task)  

#表单提交
@hello.route("/test/register") # 网页路径
def register():
    return render_template("test/register.html")  #文件结构


#接受表单的路由 需要指定的method -- post
@hello.route("/result", methods=['POST','GET'] ) # 网页路径
def result():
    if request.method == 'POST':
        result = request.form   #返回这个字典

        return render_template("test/result.html",result=result)
    else:
        return "error!"
    

if __name__ == "__main__":
    hello.run(debug=True)  #  启动服务器
