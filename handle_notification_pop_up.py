from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Configure Chrome options to disable notifications
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")

driver = webdriver.Chrome(service=serv_obj,options=ops)

driver.get("https://whatmylocation.com")
driver.maximize_window()

