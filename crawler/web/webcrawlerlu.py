from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(
    executable_path='D:\GitHub\Spanish-university-majors-information-crawler\source\web\chromedriver.exe', options=chrome_options)


for i in range(0, 1000):
    driver = webdriver.Chrome(
        executable_path='D:\GitHub\Spanish-university-majors-information-crawler\source\web\chromedriver.exe', options=chrome_options)

    driver.get('https://www.toutoupiao.com/Vote/58943?PageIndex=1')

    time.sleep(2)
    driver.find_element("id", "445748").click()
    print(i)
    time.sleep(2)
    driver.quit()
    time.sleep(1)
