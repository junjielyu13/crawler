from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(
    executable_path='D:\GitHub\Spanish-university-majors-information-crawler\source\web\chromedriver.exe', options=chrome_options)

driver.get('https://www.baidu.com')
driver.find_element("id", "kw").send_keys('python')
driver.find_element("id", "su").click()

# print(driver.page_source)
print(driver.title)


driver.quit()
