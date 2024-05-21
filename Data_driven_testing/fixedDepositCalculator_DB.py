import psycopg2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj, options=ops)
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

try:
    connection = psycopg2.connect(
        user="postgres",
        password="postgres#1234",
        host="localhost",
        port="5432",
        database="practice_db"
    )

    cursor = connection.cursor()
    cursor.execute("select * from caldata")

    rows = cursor.fetchall()

    for row in rows:
        pric = row[0]
        rateofinterest = row[1]
        per1 = row[2]
        per2 = row[3]
        fre = row[4]
        exm_value = row[5]

        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        perioddrp.select_by_visible_text(per2)

        fredrop = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        fredrop.select_by_visible_text(fre)

        driver.find_element(By.XPATH, "//div[@class='CTR PT15']/child::a[1]").click()

        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        if float(exm_value) == float(act_mvalue):
            print("test passed")
        else:
            print("test failed")

        driver.find_element(By.XPATH, "//img[@class='PL5']").click()
        time.sleep(2)

    connection.close()

except:
    print("Connection unsuccessfull.......")

driver.close()
