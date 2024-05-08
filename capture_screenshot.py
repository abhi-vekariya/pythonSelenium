from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://www.orangehrm.com/")
driver.maximize_window()

# driver.save_screenshot(os.getcwd() + '/new.png')

# driver.get_screenshot_as_file(os.path.join(os.getcwd(), "new1.png"))




