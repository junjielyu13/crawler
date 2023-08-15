#-*- codeing = utf-8 -*-
#@Time : 29/1/2021
#@Author : Junjie Li
#@File : testUrllib.py
#@Software : Vscode

import urllib.request
# 获取一个get请求
'''
response = urllib.request.urlopen("https://www.baidu.com")
print(response.read().decode('utf-8'))   #查看网页源代码 对获取到的网页源码进行解码
'''

# 获取一个post请求  : 模拟用户真实登入的请求
# http://httpbin.org/post

'''
  import urllib.parse
  date = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")  # 用户名密码，coorki信息
  response = urllib.request.urlopen("http://httpbin.org/post",data=date)
  print(response.read().decode("utf-8")) 
'''
'''
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "hello": "world"
  },
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "11",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Python-urllib/3.8",
    "X-Amzn-Trace-Id": "Root=1-60144d02-6e9899f256667c0076a92783"
  },
  "json": null,
  "origin": "93.176.134.73",
  "url": "http://httpbin.org/post"
}
'''

# 超时处理
'''
try:
  response = urllib.request.urlopen("http://httpbin.org/get",timeout=5)
  print(response.read().decode("utf-8")) 
except urllib.error.URLError as e: # 遇到其他用，来分隔
  print("time out")
'''
'''
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.8", 
    "X-Amzn-Trace-Id": "Root=1-60145619-7793c9e21e5addf6364c0edd"
  },
  "origin": "93.176.134.73",
  "url": "http://httpbin.org/get"
}
'''

'''
response = urllib.request.urlopen("http://douban/get")
print(response.status) # 200 表示正常 状态码 # 418 被发现是爬虫 # 404 找不到
'''

'''
response = urllib.request.urlopen("http://www.baidu.com")
print(response.getheader("P3p")) #还可以请求其他东西
'''

'''
url = "https://httpbin.org/post"
headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding = "utf-8" )
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
responose = urllib.request.urlopen(req)
print(responose.read().decode("utf-8"))
'''
'''
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "name": "eric"
  },
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-60145d47-7674bb972d09c7c63ed355de"
  },
  "json": null,
  "origin": "93.176.134.73",
  "url": "https://httpbin.org/post"
}
'''

url = "https://www.baidu.com/"
headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
req = urllib.request.Request(url=url, headers=headers)
responose = urllib.request.urlopen(req)
print(responose.read().decode("utf-8"))

# html 格式的网页