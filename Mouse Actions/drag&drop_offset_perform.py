import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.globalsqa.com/demoSite/practice/slider/range.html")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
print(min_slider.location) #{'x': 274, 'y': 46}

max_slider = driver.find_element(By.XPATH,"//span[2]")
print(max_slider.location)

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,30, 0).perform()
act.drag_and_drop_by_offset(max_slider,-100,0).perform()

print(min_slider.location)
print(max_slider.location)

