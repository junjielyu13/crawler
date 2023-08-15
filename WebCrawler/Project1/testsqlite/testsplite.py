
#-*- codeing = utf-8 -*-
#@Time : 29/1/2021
#@Author : Junjie Li
#@File : testsplite.py
#@Software : Vscode


import sqlite3


# 1.链接数据库
'''
coon = sqlite3.connect("test.db")  #打开或者创建一个数据库文件

print("Opened datebase succfully")  
'''


# 2.创建数据表
'''
conn = sqlite3.connect("test.db") 

print("Opened datebase succfully")  

c = conn.cursor()  #获取游标

sql = '''
#    create table company 
#        (id int not null
#            primary key not null, 
#        name text not null,
#        age int not null,
#        address char(50),
#        salary real); 
'''

c.execute(sql)     #执行sql语句
conn.commit()      #提取数据库操作
conn.close()       #关闭数据库链接

print("creat table succfully")
'''

# 3. 插入数据
'''
conn = sqlite3.connect("test.db") 

print("Opened datebase succfully")  

c = conn.cursor()  #获取游标

sql1 = '''
#   insert into company (id, name, age , address, salary)  #插入数据
#   values (1, "junjie", 32, "beijing", 80000);
#'''

#sql2 = '''
#    insert into company (id, name, age , address, salary)
#    values (2, "cm", 12, "barcelona", 180000)
'''



c.execute(sql1)
c.execute(sql2)      #执行sql语句


conn.commit()      #提取数据库操作
conn.close()       #关闭数据库链接

print("插入数据完毕")
'''




# 4.查询数据


conn = sqlite3.connect("test.db") 

print("Opened datebase succfully")  

c = conn.cursor()  #获取游标


sql = "select id, name, address, salary from company"

cursor = c.execute(sql)      #执行sql语句

for row in cursor:
    print("id =", row[0])
    print("name =", row[1])
    print("address =", row[2])
    print("salary =", row[3],"\n")

conn.close()       #关闭数据库链接

print("查询数据完毕")
