import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//button[normalize-space()='Alert']").click()

alertbox = driver.switch_to.alert

print(alertbox.text)

alertbox.accept()

time.sleep(2)
driver.close()