from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'MRF Ltd')]/self::a").text
# print(text_msg)

#parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'MRF Ltd')]/parent::td").text
# print(text_msg)

#child
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr/child::td").text
# print(text_msg)

#ancestor
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr").text
# print(text_msg)

#descendant
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr/descendant::td")
# print(len(descendants))

#following
# followings = driver.find_elements(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr/following::*")
# print(len(followings))

#following-siblings
# followings_sib = driver.find_elements(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr/following-sibling::*")
# print(len(followings_sib))

#preceding
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr/preceding::*")
# print(len(precedings))

#preceding-siblings
# precedings_sib = driver.find_elements(By.XPATH, "//a[contains(text(),'MRF Ltd')]/ancestor::tr/preceding-sibling::*")
# print(len(precedings_sib))

driver.close()

