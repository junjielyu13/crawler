#-*- codeing = utf-8 -*-
#@Time : 29/1/2021
#@Author : Junjie Li
#@File : 16sqlite.py
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
    baseurl = "https://movie.douban.com/top250?start="

    # 1.爬取网页
    datalist = getDate(baseurl) 
    dbpath = "movie.db"
    # askURL(baseurl)

    # 3.保存数据
    saveDateDb(datalist,dbpath)


findLink = re.compile(r'<a href="(.*?)"') # 创建正则表达式对象，表示规则 -- 字符串的模式
#影片的链接的规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S) 
#图片的链接的规则
findTitle = re.compile(r'<span class="title">(.*)</span>')
#片名
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')
#概识
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
#影片的相关内容

# 1.爬取网页
def getDate(baseurl):

    datalist  = []

    for i in range(0,10):  # 调用信息的函数 一页25个 * 10次  == 250
        url = baseurl + str(i*25)
        html = askURL(url) # 保存获取到的网页源码
    
        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串,形成列表 # div 同时有class属性
            # print(item)  # test 查看电影item全部信息
            
            date = []  #保存一部电影的全部信息
            item = str(item)

            #print(item)
            #break   #查看单个段

            link = re.findall(findLink,item)[0]  #re库用来查找，通过正则表达式查找指定的字符串 [0] 表示两个里面的第一个
            # print(link)  # 影片的链接
            date.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            date.append(imgSrc)

            titles = re.findall(findTitle,item) # 片面只有一个中文名 不用[0]
            if(len(titles) == 2):
                ctitle = titles[0]  
                date.append(ctitle) # 中文名
                otitle = titles[1].replace("/","") # 去掉无关的符号
                date.append(otitle) # 外国名
            else:
                date.append(titles[0])
                date.append(' ') # 空 外国名

            rating = re.findall(findRating,item)[0]
            date.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            date.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")  # 去掉句号
                date.append(inq)
            else:
                date.append(" ") #  空 概识

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) # 去掉 <br/>
            bd = re.sub('/'," ",bd)     
            date.append(bd.strip())  #去掉前后的空格


            datalist.append(date) #把处理好的一部电影信息放进去
                
    # print(datalist)
    return datalist

#得到指定一个url的网页内容
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

# 3.保存数据
def saveDateDb(datalist, dbpath):

    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250(
                info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        print(sql) # 查看插入
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()


def init_db(dbpath):

    sql = '''
        create table movie250 
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varcahr, 
        score numeric,
        rated numeric,
        instroduction text,
        info text
        )

    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



if __name__ == "__main__":
   main()
   #init_db("testmovie.db")
   print("finsh")