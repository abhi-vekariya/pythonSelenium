from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import os
firefox_binary_path = '/usr/bin/firefox'
download_location = os.getcwd()
def firefox_setup():
    serv_obj = Service("/home/abhivekariya/driver_for_browser/firefox/geckodriver")
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    firefox_options.set_preference("browser.download.manager.showWhenStarting",False)
    firefox_options.set_preference("browser.download.folderList",2) # 0-desktop, 1- download folder, 2- desired location
    firefox_options.set_preference("browser.download.dir",download_location)

    driver = webdriver.Firefox(firefox_binary=firefox_binary_path,service=serv_obj,options=firefox_options)
    return driver

driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()


