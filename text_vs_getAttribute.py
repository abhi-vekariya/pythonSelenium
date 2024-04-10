from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com/login?returnUrl=%2Flogin")
driver.maximize_window()

email = driver.find_element(By.XPATH,"//input[@id='Email']")
email.clear()

email.send_keys("sim@gmail.com")

print("using text:", email.text) #it return inner text of element
print("using get_attribut:", email.get_attribute("value")) #it gives value of any attribute
print("using get_attribute:", email.get_attribute("name"))

driver.quit()