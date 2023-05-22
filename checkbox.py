from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.find_element(By.ID, "checkBoxOption3").click()
# driver.find_element(By.CSS_SELECTOR,"label input[value='option1']").click()
options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for option in options:
    if option.get_attribute("value") == "option3":
        option.click()
        print(option.is_selected())