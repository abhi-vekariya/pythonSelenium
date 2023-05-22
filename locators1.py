from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
#Here we are getting one form and automate that
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Name
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Vikas")
#Email
driver.find_element(By.NAME, "email").send_keys("abhi@google.com")
#Password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abhiRRR")
#Checkbox
driver.find_element(By.ID, "exampleCheck1").click()

#Static Dropdown option selection
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_index(2)
dropdown.select_by_visible_text("Female")

#Submit button
driver.find_element(By.XPATH, "//input[@type='submit']").click()


driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello World")
# driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

#Success-Message
message = driver.find_element(By.CLASS_NAME,"alert-dismissible").text
assert "Success" in message


