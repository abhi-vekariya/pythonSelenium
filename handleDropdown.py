from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drp_countries = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

drp_countries.select_by_visible_text("India")
drp_countries.select_by_value("10")
drp_countries.select_by_index(10)

# alloptions = drp_countries.options
#
# for option in alloptions:
#     if option.text == "India":
#         option.click()
#         break


alloptions = driver.find_elements(By.XPATH, "//select[@id='input-country']/option")


