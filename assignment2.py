import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

expected_list = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actual_list = []

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
driver.maximize_window()


driver.find_element(By.XPATH, "//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)

vegetables = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(vegetables) > 0

for vegetable in vegetables:
    vegi_name = vegetable.find_element(By.CSS_SELECTOR, "h4.product-name").text
    actual_list.append(vegi_name)

assert expected_list == actual_list





