from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

cookies = driver.get_cookies()

driver.add_cookie({'name': 'simform','value':'software'})

# driver.delete_cookie('simform')
#
# driver.delete_all_cookies()

cookies1 = driver.get_cookies()

for c in cookies1:
    print(c.get('name'))

driver.close()


