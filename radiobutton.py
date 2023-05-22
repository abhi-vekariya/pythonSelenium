from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()
# for button in radio_buttons:
#     if button.get_attribute("value") == "radio3":
#         button.click()
#         assert button.is_selected()
#         break

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


