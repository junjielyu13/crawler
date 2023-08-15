

#-*- codeing = utf-8 -*-
#@Time : 31/1/2021
#@Author : Junjie Li
#@File : testKeyword.py
#@Software : Vscode

from urllib import parse

keyword = parse.quote("大数据")   #编码
print(keyword)
# %E5%A4%A7%E6%95%B0%E6%8D%AE
newKW = parse.quote(keyword)  #二次编码
print(newKW)
#%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE

def main():
    kw = input (" search == _: ")
    keyword = parse.quote(parse.quote(kw))
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,"+keyword+".html"
    print(url)

if __name__ == "__main__":
    main()
