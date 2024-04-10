from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# For Chrome
service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

#For Firefox
# service_obj = Service("/home/abhivekariya/driver_for_browser/firefox/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

#For Edge
# service_obj = Service("/home/abhivekariya/driver_for_browser/edge/msedgedriver")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.current_url)

driver.back()
driver.refresh()
driver.forward()

#driver close all windows of browser
driver.close()
