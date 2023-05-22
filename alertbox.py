import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = 'Simform'
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
assert name in alerttext
time.sleep(2)
alert.accept()

driver.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
time.sleep(2)
alert.dismiss()
