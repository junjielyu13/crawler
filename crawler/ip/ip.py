from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.page_load_strategy = 'eager'

# api_url = 'http://http.tiqu.alibabaapi.com/getip3?num=1&amp;type=3&amp;pack=63620&amp;port=1&amp;lb=1&amp;pb=4&amp;gm=4&amp;regions='

# chrome_options.add_argument(
#     "--proxy-server-http://61.135.217.7:80")  # 设定代理ip地址

# https://free-proxy-list.net/s

# ip = "134.238.252.143"
# port = "8080"

ip = "124.90.13.131"
port = "8085"

chrome_options.add_argument(
    "--proxy-server=http://"+ip+":" + port)  # 设定代理ip地址

driver = webdriver.Chrome(
    executable_path='D:\GitHub\Spanish-university-majors-information-crawler\source\web\chromedriver.exe', options=chrome_options)


# proxy = driver.get(api_url)


# driver.get("http://httpbin.org/ip")  # 注意这里http://httpbin.org/ip 是返回IP的网址
driver.get('https://www.wenjuan.com/s/qMB3mer/')

# count = 1x
# while True:
#  for i in range(0, 2000):

# time.sleep(2)
# driver.find_element(By.XPATH,
# 、                     '//*[@id="question-63b72d8abac485c0c39808ba_63b73eaffb0723c4ec50bf13"]/div[2]/div[2]/div[2]/div[2]').click()
driver.find_element(By.XPATH,
                    '//*[@id="question-63b72d8abac485c0c39808ba_63b73e855d2f82c1603dc4a8"]/div[2]/div[2]/div[2]/div[2]').click()
driver.find_element(By.XPATH,
                    '//*[@id="question-63b72d8abac485c0c39808ba_63b73e7bbac485c0c218c41e"]/div[2]/div[2]/div[2]/div[2]').click()
# driver.find_element("id", "445747").click()
# driver.find_element("id", "445747").click()
# driver.find_element("id", "445747").click()


# print(time.strftime('%H:%M:%S', time.localtime()))
# print(count)
# count += 1

# time.sleep(2)
# driver.quit()
# time.sleep(1)
