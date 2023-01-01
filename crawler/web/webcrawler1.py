from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(
    executable_path='D:\GitHub\Spanish-university-majors-information-crawler\source\web\chromedriver.exe', options=chrome_options)

driver.get('https://www.toutoupiao.com/Vote/58943?PageIndex=1')
for i in range(0, 100):

    # driver.find_element("id", "kw").send_keys('python')
    # driver.find_element("id", "su").click()

    # driver.get('https://www.toutoupiao.com/Vote/58943?PageIndex=2')
    # driver.find_element("id", "kw").send_keys('python')
    # driver.find_element("id", "su").click()

    # print(driver.page_source)
    # print(driver.title)
    time.sleep(2)
    driver.find_element("id", "445747").click()

    # driver.find_element("id", "445155").click()
    # time.sleep(2)

    # driver.get('https://www.toutoupiao.com/Vote/58943?PageIndex=2')

    # driver.find_element("id", "445848").click()
    # time.sleep(2)

    print(i)
    # driver.get('https://www.toutoupiao.com/Vote/58943?PageIndex=2')
    time.sleep(2)
    driver.refresh()

driver.quit()
