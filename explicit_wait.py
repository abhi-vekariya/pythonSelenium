from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=Exception)

driver.get("https://www.google.com")
driver.maximize_window()

searchbox = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
searchbox.send_keys("Selenium")
searchbox.submit()

searchLink = mywait.until(EC.presence_of_element_located((By.XPATH,"//a[@href='https://www.selenium.dev/']//h3[@class='LC20lb MBeuO DKV0Md'][normalize-space()='Selenium']")))
searchLink.click()

driver.quit()


