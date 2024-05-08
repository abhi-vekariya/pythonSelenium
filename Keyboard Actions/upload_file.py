from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://tus.io/demo")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='P0-0']").send_keys("/home/abhivekariya/Dummy/jpg/bp-miller-rGDv4llw-mk-unsplash.jpg")
