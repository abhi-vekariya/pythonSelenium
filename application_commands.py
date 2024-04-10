from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


print(driver.title)  #OrangeHRM
print(driver.current_url)  #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)

driver.close()


