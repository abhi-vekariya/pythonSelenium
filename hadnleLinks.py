from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME,"a")
count = 0
for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(url, " is broken")
        count += 1
    else:
        print(url," is valid")

print("total number of broken links: ", count)

