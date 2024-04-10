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

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

links = driver.find_elements(By.XPATH, "(//div[@id='wikipedia-search-result-link'])/a")

for link in links:
    link.click()

windowIds = driver.window_handles

for winId in windowIds:
    driver.switch_to.window(winId)
    print(driver.title)


# time.sleep(3)
driver.quit()