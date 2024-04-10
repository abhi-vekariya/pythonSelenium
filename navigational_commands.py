import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.myntra.com")
driver.maximize_window()

driver.get("https://www.flipkart.com")

driver.back()

time.sleep(1)

driver.forward()

driver.refresh()


time.sleep(2)
driver.close()