
#-*- codeing = utf-8 -*-
#@Time : 31/1/2021
#@Author : Junjie Li
#@File : doubanhtml.py
#@Software : Vscode

import os 
import sys
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import xlwt
import sqlite3   


def main():
    baseurl = "https://book.douban.com/top250?start="
    html = askURL(baseurl)
    print(html)

    # 1.爬取网页

def askURL(url): 

    # 模拟浏览器head信息，向豆瓣服务器发送消息
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
    #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器,浏览器 (本质上是告诉浏览器，我们可以接受什么水平的信息)
    
    resquet = urllib.request.Request(url,headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(resquet)
        html = response.read().decode("utf-8")
        # print(html) # 查看网页
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html


if __name__ == "__main__":
   main()
   print("finsh")