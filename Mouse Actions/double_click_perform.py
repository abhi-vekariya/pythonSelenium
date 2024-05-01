from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demoqa.com/buttons")

double_click_button = driver.find_element(By.XPATH,"//button[@id='doubleClickBtn']")

act = ActionChains(driver)
act.double_click(double_click_button).perform()