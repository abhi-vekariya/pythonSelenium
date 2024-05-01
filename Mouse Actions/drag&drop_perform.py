import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.seleniumeasy.com/drag-and-drop-demo.html")
driver.maximize_window()

try:
    option_1_source = driver.find_element(By.XPATH,"//span[normalize-space()='Draggable 1']")
    option_1_destination = driver.find_element(By.XPATH, "//div[@id='mydropzone']")
    act = ActionChains(driver)
    act.drag_and_drop(option_1_source,option_1_destination).perform()

    option_2_source = driver.find_element(By.XPATH,"//span[normalize-space()='Draggable 2']")
    option_2_destination = driver.find_element(By.XPATH,"//div[@id='mydropzone']")
    act.drag_and_drop(option_2_source,option_2_destination).perform()
    print("Drag-and-drop action performed successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    time.sleep(3)
    # Close the browser window
    driver.quit()