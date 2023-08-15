
#-*- codeing = utf-8 -*-
#@Time : 31/1/2021
#@Author : Junjie Li
#@File : doubanbookExcel.py
#@Software : Vscode


import os 
import sys
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import xlwt
import sqlite3
import numpy as np   


def main():
    baseurl = "https://book.douban.com/top250?start="

    # 1.爬取网页
    datalist = getDate(baseurl) 
    savepath = "doubanbook_TOP250.xls"
    # askURL(baseurl)
    #print(datalist[0][0][0])

    # 3.保存数据
    saveDate(datalist, savepath)


findLink = re.compile(r'<a class="nbg" href="(.*?)"') # 创建正则表达式对象，表示规则 -- 字符串的模式
#图书的链接的规则
findTitleOut = re.compile(r'<span style="font-size:12px;">(.*?)</span>')
#外国片名
findRating = re.compile(r'<span class="rating_nums">(.*)</span>')
#评分                     
findJudge = re.compile(r'<span class="pl">(.*?)</span>',re.S)
#评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')
#概识
findBd = re.compile(r'<p class="pl">(.*?)</p>',re.S)
#图书的相关内容

# 1.爬取网页
def getDate(baseurl):

    listAll = []
    datalist  = []
    datalistImgSrc = []
    datalisttitleCs = []
    for i in range(0,10):  # 调用信息的函数 一页25个 * 10次  == 250
        url = baseurl + str(i*25)
        html = askURL(url) # 保存获取到的网页源码

        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("tr", class_="item"):  # 查找符合要求的字符串,形成列表 #div 同时有class属性

            date = []  #保存一部图书的全部信息
            item = str(item)
            #print(item)            # test 查看图书item全部信息
            #break   #查看单个段
            

            link = re.findall(findLink,item)[0]  #re库用来查找，通过正则表达式查找指定的字符串 [0] 表示两个里面的第一个
            #print(link)  # 图书的链接
            date.append(link)  


            titles = re.findall(findTitleOut,item)  #图书另名
            if len(titles) == 0:
                #print("null")
                date.append(" ")
            else:
                title = titles[0]
                secondtitle = title.split(" : ")
                if len(secondtitle[0]) == 0:
                    #print(secondtitle[1])
                    date.append(secondtitle[1])
                else:
                    #print(secondtitle[0])
                    date.append(secondtitle[0])

            rating = re.findall(findRating,item)[0]  #评分
            #print(rating)
            date.append(rating)


            judgeNum = re.findall(findJudge,item)[0] #评价人数
            x = judgeNum.replace("\n", "")  
            y = x.replace("(","")
            z = y.replace(")","")
            t = z.replace(" ","")
            #print(t)
            date.append(t)


            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")  # 去掉句号
                #print(inq)
                date.append(inq)
            else:
                #print("null inq")
                date.append(" ") #  空 概识


            bd = re.findall(findBd,item)[0]  #书本基本信息
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd) # 去掉 <br/>
            bd = re.sub('/'," ",bd)     
            #print(bd)
            date.append(bd.strip())  #去掉前后的空格

            datalist.append(date) #把处理好的一部电影信息放进去


        imgSrcs = soup.select(".nbg > img")  #html解剖
        for imgSrc in imgSrcs:
            #print(imgSrc["src"]) #图书图片链接
            datalistImgSrc.append(imgSrc["src"])

            
        
        titleCs = soup.select(".pl2 > a")  #html解剖
        for titleC in titleCs:
            #print(titleC["title"]) #图书中文名 
            datalisttitleCs.append(titleC["title"])    

    listAll.append(datalist)
    listAll.append(datalistImgSrc)
    listAll.append(datalisttitleCs)
    return listAll

#Get the content of a webpage specified by a url
def askURL(url): 

    # Simulate the browser head coorki information and send a message to the web server
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
def saveDate(datalist, savepath):

    print("Excel save...")

    book = xlwt.Workbook(encoding="utf-8", style_compression=0 ) # 创建workbook对象
    sheet = book.add_sheet('douban book top 250', cell_overwrite_ok=True )  #创建工作表
    col =("图书详情", "图片链接" , "图书中文名" , "图书外国名" , "评分", "评论数", "概识" , "相关信息")
    #      0             1 ?         2 ?             3           4      5         6       7
    for i in range (0,8):
        sheet.write(0,i,col[i]) # 列名
    
    datainfo = datalist[0]
    for i in range(0,250):
        print("第%d条"%i) 
        sheet.write(i+1,1,datalist[1][i])
        sheet.write(i+1,2,datalist[2][i])
        sheet.write(i+1,0,datalist[0][i][0])  #数据
        sheet.write(i+1,3,datalist[0][i][1])
        sheet.write(i+1,4,datalist[0][i][2])
        sheet.write(i+1,5,datalist[0][i][3])
        sheet.write(i+1,6,datalist[0][i][4])
        sheet.write(i+1,7,datalist[0][i][5])

            
    book.save(savepath) #保存数据



if __name__ == "__main__":
   main()
   print("finsh")