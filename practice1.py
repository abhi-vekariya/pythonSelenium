from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1st Approach
# countries_drp = driver.find_elements(By.XPATH,"//select[@id='country']/option")
#
# for country in countries_drp:
#     if country.text == 'Brazil':
#         country.click()
#         break

#2nd Approach : by using Select class
countries = Select(driver.find_element(By.XPATH,"//select[@id='country']"))
countries.select_by_visible_text("India")
countries.select_by_value("japan")
countries.select_by_index(2)

options = countries.options

for option in options:
    print(option.get_attribute('value'))


