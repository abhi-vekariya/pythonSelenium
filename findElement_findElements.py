import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.nopcommerce.com")

#Working with find_element
# locator matching with single webelement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple")

# locator matching with multiple webelements
# link_element=driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(link_element.text)

#locator not matching with any element
# not_matched_element =  driver.find_element(By.LINK_TEXT,"Log")
# print(not_matched_element) #it gives error as we can't find that element

#Working with find_elements
#when locator match single element
# elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(elements[0].send_keys("Apple")) #find_elements gives us List

#when locator matches multiple elements
multi_elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(multi_elements))
for ele in multi_elements:
    print(ele.text)

#when locator doesn't find any element
# no_element = driver.find_elements(By.LINK_TEXT,"Log")
# print(len(no_element)) #it's not giving any exception like find_element do, just giving 0 if not any element in List

driver.close()






