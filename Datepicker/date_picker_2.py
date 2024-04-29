from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='departon']").click()

dropdown_month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
dropdown_month.select_by_visible_text("Dec")

dropdown_year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
dropdown_year.select_by_visible_text("2025")

days = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for day in days:
    if day.text == '25':
        day.click()
        break





