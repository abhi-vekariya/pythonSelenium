from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

download_directory = os.getcwd()

def chrome_setup():
    serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")

    prefs = {"download.default_directory": download_directory}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=serv_obj, options=chrome_options)
    return driver

driver = chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()