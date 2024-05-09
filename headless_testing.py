from selenium import webdriver

# headless is fast in performance & it don't open site, just work in backend
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    driver = webdriver.Chrome(service=serv_obj,options=chrome_options)
    return driver

# def headless_edge():
#     from selenium.webdriver.edge.service import Service
#     serv_obj = Service("/home/abhivekariya/driver_for_browser/edge/msedgedriver")
#     edge_options = webdriver.EdgeOptions()
#     edge_options.headless = True
#     driver = webdriver.Chrome(service=serv_obj,options=edge_options)
#     return driver

# def headless_firefox():
#     from selenium.webdriver.edge.service import Service
#     serv_obj = Service("/home/abhivekariya/driver_for_browser/firefox/geckodriver")
#     firefox_options = webdriver.FirefoxOptions()
#     firefox_options.headless = True
#     driver = webdriver.Chrome(service=serv_obj,options=firefox_options)
#     return driver

driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")

print(driver.title)
print(driver.current_url)
