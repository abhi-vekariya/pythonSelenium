from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("abhi@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input ").send_keys("abhi#1111")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("abhi#1111")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.CSS_SELECTOR, "form div:nth-child(4) button").click()
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


