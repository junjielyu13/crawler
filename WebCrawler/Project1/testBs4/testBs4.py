#-*- codeing = utf-8 -*-
#@Time : 29/1/2021
#@Author : Junjie Li
#@File : testBs4.py
#@Software : Vscode


from bs4 import BeautifulSoup

'''
BeautifulSoup4 将复杂的html文档转换成一个复杂的树形结构，每个节点都是python对象，可以归纳为4种对象

--Tag
--NavigableString
--Beautifulsoup
--Comment
'''

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")


# 1.Tag : 标签及其内容: 拿到他的第一个内容

# print(bs.title) 
'''
<title>
豆瓣电影 Top 250
</title>
'''
# print(bs.a)
'''
<a class="nav-login" href="https://accounts.douban.com/passport/login?source=movie" rel="nofollow">登录/注册</a>
'''

# print(bs.head)
'''
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="webkit" name="renderer"/>
<meta content="always" name="referrer"/>
<meta content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" name="google-site-verification">
<title> 豆瓣电影 Top 250 </title>
<meta content="cZdR4xxR7RxmM4zE" name="baidu-site-verification">
<meta content="no-cache" http-equiv="Pragma"/>
<meta content="Sun, 6 Mar 2005 01:00:00 GMT" http-equiv="Expires"/>
<link href="https://img9.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png" rel="apple-touch-icon"/>    
<link href="https://img9.doubanio.com/f/shire/859dba5cddc7ed1435808cf5a8ddde5792cd6e0c/css/douban.css" rel="stylesheet" type="text/css"/>
<link href="https://img9.doubanio.com/f/shire/db02bd3a4c78de56425ddeedd748a6804af60ee9/css/separation/_all.css" rel="stylesheet" type="text/css"/>  
<link href="https://img9.doubanio.com/f/movie/252bef058b97005c6a41e8f1b9f7b06b84bc71b3/css/movie/base/init.css" rel="stylesheet"/>
<script type="text/javascript">var _head_start = new Date();</script>
<script src="https://img9.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js" type="text/javascript"></script> <script src="https://img9.doubanio.com/f/shire/5ecaf46d6954d5a30bc7d99be86ae34031646e00/js/douban.js" type="text/javascript"></script>
<script src="https://img9.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js" type="text/javascript"></script>     
<link href="https://img9.doubanio.com/f/movie/2c95f768ea74284b900c04c0209b0a44f0a0de52/css/movie/top_movies.css" rel="stylesheet" type="text/css"><script data-cfg-autoload="false" src="https://img9.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" type="text/javascript"></script>
<script type="text/javascript">
    Do.ready(function(){
            $("#mine-selector input[type='checkbox']").click(function(){
                var val = $(this).is(":checked")?$(this).val():"";
                window.location.href = '/top250?filter=' + val;
            })
    })
</script>
<style type="text/css">
.site-nav-logo img{margin-bottom:0;}
</style>
<style type="text/css">img { max-width: 100%; }</style>
<script type="text/javascript"></script>
<link href="https://img9.doubanio.com/misc/mixed_static/562925b5e3824700.css" rel="stylesheet"/>
<link href="https://img9.doubanio.com/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
</link></meta></meta></head>
'''



# 2. NavigableString 标签里的内容(string)

# print(bs.title.string)
'''
豆瓣电影 Top 250
'''
# print(bs.a.attrs) 
'''
 {'href': 'https://accounts.douban.com/passport/login?source=movie', 'class': ['nav-login'], 'rel': ['nofollow']}
'''





# 3.BeautifulSoup   表示整个文档
# print(type(bs)) 
'''
<class 'bs4.BeautifulSoup'>
'''
# print(bs.name)
'''
[document]
'''
# print(bs.attrs)
'''
{}
'''
# print(bs) # 整个文档






# 4.Comment 是一个特殊的NavigableString 输出内容不包含注释符号
#print(bs.a.string)
'''
登录/注册
'''
#print(type(bs.a.string))
'''
<class 'bs4.element.NavigableString'>
'''

#-------------------------------------------------------------
#应用
#文档的遍历

# print(bs.head.contents) # type list
'''
[
'\n', <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>, '\n', <meta content="webkit" name="renderer"/>, '\n', <meta content="always" name="referrer"/>, '\n', <meta content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" name="google-site-verification">
<title> 豆瓣电影 Top 250 </title>
<meta content="cZdR4xxR7RxmM4zE" name="baidu-site-verification">
<meta content="no-cache" http-equiv="Pragma"/>
<meta content="Sun, 6 Mar 2005 01:00:00 GMT" http-equiv="Expires"/>
<link href="https://img9.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png" rel="apple-touch-icon"/>
<link href="https://img9.doubanio.com/f/shire/859dba5cddc7ed1435808cf5a8ddde5792cd6e0c/css/douban.css" rel="stylesheet" type="text/css"/>
<link href="https://img9.doubanio.com/f/shire/db02bd3a4c78de56425ddeedd748a6804af60ee9/css/separation/_all.css" rel="stylesheet" type="text/css"/>
<link href="https://img9.doubanio.com/f/movie/252bef058b97005c6a41e8f1b9f7b06b84bc71b3/css/movie/base/init.css" rel="stylesheet"/>
<script type="text/javascript">var _head_start = new Date();</script>
<script src="https://img9.doubanio.com/f/movie/0495cb173e298c28593766009c7b0a953246c5b5/js/movie/lib/jquery.js" type="text/javascript"></script> <script src="https://img9.doubanio.com/f/shire/5ecaf46d6954d5a30bc7d99be86ae34031646e00/js/douban.js" type="text/javascript"></script>
<script src="https://img9.doubanio.com/f/shire/0efdc63b77f895eaf85281fb0e44d435c6239a3f/js/separation/_all.js" type="text/javascript"></script>
<link href="https://img9.doubanio.com/f/movie/2c95f768ea74284b900c04c0209b0a44f0a0de52/css/movie/top_movies.css" rel="stylesheet" type="text/css"><script data-cfg-autoload="false" src="https://img9.doubanio.com/f/shire/77323ae72a612bba8b65f845491513ff3329b1bb/js/do.js" type="text/javascript"></script>
<script type="text/javascript">
    Do.ready(function(){
            $("#mine-selector input[type='checkbox']").click(function(){
                var val = $(this).is(":checked")?$(this).val():"";
                window.location.href = '/top250?filter=' + val;
            })
    })
</script>
<style type="text/css">
.site-nav-logo img{margin-bottom:0;}
</style>
<style type="text/css">img { max-width: 100%; }</style>
<script type="text/javascript"></script>
<link href="https://img9.doubanio.com/misc/mixed_static/562925b5e3824700.css" rel="stylesheet"/>
<link href="https://img9.doubanio.com/favicon.ico" rel="shortcut icon" type="image/x-icon"/>
</link></meta></meta>
]
'''

# print(bs.head.contents[1]) # beautifulsoup 遍历文档树
'''
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
'''

#文档的搜索

#1.findAll()
# string过滤: 会查找与string完全匹配的内容
# t_list = bs.findAll("a") #查找所有的"a"

#2.正则表达式: 使用search() 用来匹配内容
import re
# t_list = bs.findAll(re.compile("a"))  # 包含a 都可以显示出来， 某一个标签及其内容 只要标签里面含a 其子内容都表达出来 

#3.方法: 根据函数的要求来查找
'''
def name_is_exists(tag):
    return tag.has_attr("name")
t_list = bs.find_all(name_is_exists)

for item in t_list:
    print(item)
'''
#print(t_list)

#2.kwargs 参数
'''
# t_list = bs.find_all(id="head")

# t_list = bs.find_all(class_=True) # 及其子内容都会出来

# t_list = bs.find_all( href="https://www.douban.com/doubanapp/frodo")
#for item in t_list:
#    print(item)
'''

#3. text 参数
'''
# t_list = bs.find_all(text = "豆瓣")
# t_list = bs.find_all(text = ["豆瓣","移动应用","法律声明"])
# t_list = bs.find_all(text = re.compile("\d")) # 应用正则表达式查找包含特点文本内容(标签里的字符串)
'''

# 4. limit 参数
'''
t_list = bs.find_all("a",limit = 3)
for item in t_list: 
    print(item)
'''

# css 选择器
# print(bs.select('title'))  
'''
[<title> 豆瓣电影 Top 250 </title>]  tyoe list 
'''
# t_list = bs.select('title')  通过标签来查找

'''
<title> 豆瓣电影 Top 250 </title>  type string
'''
#t_list = bs.select(".top-nav-info") #通过类名来查找
#print(t_list)

 
# t_list = bs.select("#db")  通过id来查找

#t_list = bs.select("a[class='tip-link']")  # 通过属性来查找
#print(t_list)
'''
[<a class="tip-link" href="https://www.douban.com/doubanapp/app?channel=qipao">豆瓣 <span class="version">6.0</span> 全新发布</a>]
'''

t_list = bs.select("head > title") #通过子标签来查找 
print(t_list)

t_list = bs.select(".mnav ~ .bri") #兄弟标签
print(t_list[0].get_text())
'''
for item in t_list: 
    print(item)
'''

