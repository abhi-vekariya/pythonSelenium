from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import os

download_directory = os.getcwd()

def edge_setup():
    serv_obj = Service("/home/abhivekariya/driver_for_browser/edge/msedgedriver")

    edge_options = webdriver.EdgeOptions()
    prefs = {"download.default_directory":download_directory}
    edge_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Edge(service=serv_obj, options=edge_options)
    return driver

driver = edge_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()

