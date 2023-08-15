#-*- codeing = utf-8 -*-
#@Time : 29/1/2021
#@Author : Junjie Li
#@File : testre.py
#@Software : Vscode

import re
#正则表达式 对字符串的一种模式 (判断字符串是否符合一定的标准)
'''
.  ：表示任何单个字符
[] : 字符集, 对单个字符给出取值范围 -- [abc] 表示a，b，c，[a-z]表示a到z单个字符
[^ ] ： 非字符集，对单个字符给出排除范围 -- [^ abc ]表示非a或者c或者b的单个字符
* : 前一个字符 0 次 或者 无限次扩展 -- abc* 表示 ab, abc, abcc , abccc 等
+ : 前一个字符 1 次 或者 无限次扩展 -- abc+ 表示 abc, abcc , abccc 等
? : 前一个字符 0 次 或者 1 次扩展 -- abc? 表示 ab, abc
| : 左右表达式任意一种 -- abc | def 表示 abc, def
{m} : 扩展前一个字符m次 -- ab{2}c 表示 abbc
{m , n} : 扩展前一个字符m到n次 包含n-- ab{1,2}c 表示 abc,abbc
^ : 匹配字符串开头 --  ^abc 表示 abc 且在一个字符串的开头
$ : 匹配字符串结尾 --  $abc 表示 abc 且在一个字符串的结尾
() : 分组标记，内部只能使用 | 操作符 -- (abc)表示abc , (abc|def)表示abc，def
\d : 数字, 等价于[0-9]
\w : 单个字符，等价于[a-za-z0-0_]


re库的主要功能
re.search() : 在一个字符串中查找匹配正则表达式的第一个位置, 放回match对象
re.match() ： 从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall() ： 查找字符串，以列表类型返回全部能匹配的子串
re.split() : 将一个字符串按照正则表达式匹配结果进行分隔，返回list
re.finditer() ： 查找字符串， 返回一个匹配结果的迭代类型， 每个迭代元素是match对象
re.sub() ： 在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串


修饰符
re.l : 使匹配对大小不敏感
re.L : 做本地化识别匹配
re.M : 多行匹配，影响 ^ , $ 
re.S : 使. 匹配包括换行在内的所有字符
re.U ：根据unicode字符集解析字符，这个标志影响 \w \W \b \B
re.X : 该标准通个给予你更灵活的格式以便你将正则表达式写得更易于理解
'''

pat = re.compile("AA") # 这个AA 是正则表达式 用来验证其他的字符串
m = pat.search("CBA") #search 字符串被校验的内容
print(m) # none == 不匹配  

m1 = pat.search("CBAA") #search 字符串被校验的内容
print(m1) # <re.Match object; span=(2, 4), match='AA'>  == 匹配  

m2 = pat.search("CBAACDAAADSAA") #search 字符串被校验的内容
print(m1) # <re.Match object; span=(2, 4), match='AA'>  并且只会找到第一个 

m3 = re.search("asd","Aasd") # 前面的是规则，后面是被校验的
print(m3) # <re.Match object; span=(1, 4), match='asd'>

print(re.findall("a","ASDaDFGAa")) # ['a', 'a'] 前面的字符串是规则 后面的字符是被校验的 并且找到所有的

print(re.findall("[A-Z]","ASDaDFGAa"))  #['A', 'S', 'D', 'D', 'F', 'G', 'A']

print(re.findall("[A-Z]+","ASDaDFGAa")) #['ASD', 'DFGA']


#sub

print(re.sub(r"a",r"A","abcdcasd")) # AbcdcAsd  找到小a用A用来替换
# 建议在正则表达式中，被比较的字符串加上r 不要担心转义字符的问题