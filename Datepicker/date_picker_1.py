from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

month = 'December'
year = '2024'
date = '25'

while True:
    mon = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[1]").text
    yr = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/div/span[2]").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for day in dates:
    if day.text == date:
        day.click()
        break



