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

    # 1.爬取网页
    getDate(baseurl) 
    # askURL(baseurl)

def getDate(baseurl):

    datalist  = []

    for i in range(0,1):  # 调用信息的函数 一页25个 * 10次  == 250
        url = baseurl + str(i*25)
        print(url)
        html = askURL(url) # 保存获取到的网页源码
    
        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("tr", class_="item"):  # 查找符合要求的字符串,形成列表 # div 同时有class属性
            # print(item)  # test 查看电影item全部信息
            
            date = []  #保存一部电影的全部信息
            item = str(item)
            
            imgLink = soup.select(".")
            print(imgLink)


            #print(item)
            #print("test getdate")
            datalist.append(date) 



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