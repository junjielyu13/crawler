
#-*- codeing = utf-8 -*-
#@Time : 31/1/2021
#@Author : Junjie Li
#@File : testbs.py
#@Software : Vscode

from bs4 import BeautifulSoup

file  = open("./51job.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

ediv = bs.select(".cn > h1")
for name in ediv:
    print(name["title"])
    # 大数据总监

days = bs.select(".ltype")
for day in days:
    print(day)
    #可能出现一大堆
    print(day["title"]) # xxx | xxx | xxxx | xxx | xxx |

'''
str.[n:m] 截取n:m个字符
str.split("|") 按照 | 分隔字符串为列表
str.replace("/r","") /r 换成空白
str.strip()去除前后空格 
'''

print(ediv)