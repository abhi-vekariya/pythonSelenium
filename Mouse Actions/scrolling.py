import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.geeksforgeeks.org/selenium-scrolling-a-web-page/")
driver.maximize_window()

# 1.scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# print(driver.execute_script("return window.pageYOffset;"))

# 2.scroll down by exact point (using one element)
# flag = driver.find_element(By.XPATH,"//strong[normalize-space()='5. Scroll to the top of the page:']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# print(driver.execute_script("return window.pageYOffset;"))

#3. scroll down to end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print(driver.execute_script("return window.pageYOffset;"))

time.sleep(5)

#4. scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
print(driver.execute_script("return window.pageYOffset;"))

