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

driver.switch_to.frame("frame-one796456169")
driver.find_element(By.ID,"RESULT_TextField-0").send_keys("abhi")

male_radio_label = driver.find_element(By.CSS_SELECTOR, "label[for='RESULT_RadioButton-1_0']")
female_radio_label = driver.find_element(By.CSS_SELECTOR, "label[for='RESULT_RadioButton-1_1']")

male_radio_label.click()

driver.switch_to.default_content()

time.sleep(3)
driver.close()