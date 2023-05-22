import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ger")
time.sleep(2)

dropdown_options = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
# dropdown_options = driver.find_elements(By.CLASS_NAME, "ui-menu-item")

for country in dropdown_options:
    if country.text == "Germany":
        country.click()
        break

print(driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value"))
assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value") == "Germany100", "Country name is not correct"
