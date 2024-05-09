from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

# switch to new tab
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://www.orangehrm.com/")

# switch to new window
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.orangehrm.com/")

driver.quit()
