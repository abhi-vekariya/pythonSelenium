from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)
# It's not affect speed or performance of script
driver.implicitly_wait(5)

driver.get("https://www.google.com")
driver.maximize_window()

searchbox = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']").click()
driver.quit()
