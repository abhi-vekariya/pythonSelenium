from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from  Data_driven_testing import ExcelUtils
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj, options=ops)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

file = '/home/abhivekariya/pythonSelenium/Data_driven_testing/cal_data.xlsx'

rows = ExcelUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #reading data from excel
    pric = ExcelUtils.readData(file,"Sheet1",r,1)
    rateofinterest = ExcelUtils.readData(file,"Sheet1",r,2)
    per1 = ExcelUtils.readData(file, "Sheet1", r, 3)
    per2 = ExcelUtils.readData(file, "Sheet1", r, 4)
    fre = ExcelUtils.readData(file,"Sheet1",r,5)
    exm_value = ExcelUtils.readData(file,"Sheet1",r,6)

    #passing data to application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

    perioddrp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    fredrop = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    fredrop.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//div[@class='CTR PT15']/child::a[1]").click()

    act_mvalue = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation
    if float(exm_value) == float(act_mvalue):
        print("test passed")
        ExcelUtils.writeData(file,"Sheet1",r,8,"Passed")
        ExcelUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        ExcelUtils.writeData(file,"Sheet1",r,8,"Failed")
        ExcelUtils.fillRedColor(file,"Sheet1",r,8)

    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(2)

driver.close()











