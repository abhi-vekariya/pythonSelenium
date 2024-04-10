import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

# approach 1: It selects all 7 checkboxes
# for checkbox in checkboxes:
#     checkbox.click()
#     print(checkbox.get_attribute('id'))

# approach 2: It selects all 7 checkboxes
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# time.sleep(3)

# It deselects all 7 checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()

# select specifi day
# for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname == 'monday' or weekname == 'sunday':
#         checkbox.click()

# select last 3 check box
# for i in range(len(checkboxes)-3,len(checkboxes)):
#     checkboxes[i].click()

# select first 3 check box
# for i in range(0,3):
#     checkboxes[i].click()

for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()




