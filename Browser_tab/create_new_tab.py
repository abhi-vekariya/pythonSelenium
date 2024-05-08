from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

register_link = driver.find_element(By.LINK_TEXT,"Register")

# Open register page on that same page
# register_link.click()

# open register page on second tab
register_link.send_keys(Keys.CONTROL + Keys.RETURN)


