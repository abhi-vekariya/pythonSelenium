from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("abcd")

act = ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

act.send_keys(Keys.TAB).perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
