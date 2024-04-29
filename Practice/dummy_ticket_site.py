import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

radio_buttons = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']")

desired_option = "Dummy ticket and hotel"
for radio in radio_buttons:
    option = driver.find_element(By.XPATH,"//input[@id='product_3186']").text
    if option == desired_option:
        radio.click()
        break




#     # Identify the radio buttons
#     radio_buttons = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']")
#
#     # Iterate through the radio buttons and select the desired option
#     desired_option = "Dummy ticket for Visa Application"  # Specify the option you want to select
#     for radio in radio_buttons:
#         label_text = radio.find_element(By.XPATH, "//input[@id='product_549']").text
#         print(label_text.strip())
#         if label_text.strip() == desired_option:
#             radio.click()
#             break
#
#
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
#
# finally:
#     # Close the browser window
#     time.sleep(5)
#     driver.quit()
