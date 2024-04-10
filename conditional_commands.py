from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com")
driver.maximize_window()

#is_displayed
search_button = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(search_button.is_displayed())

#is_enabled
print(search_button.is_enabled())

#is_selected : check box & radio buttons
rd_button = driver.find_element(By.XPATH, "//input[@id='pollanswers-2']")
rd_button.click()
print(rd_button.is_selected())

driver.close()
