import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

button = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
button.click()
time.sleep(3)

alertBox = driver.switch_to.alert

print(alertBox.text)
alertBox.send_keys("Hello Simform")

# alertBox.accept()

alertBox.dismiss()
