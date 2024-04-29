from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count total rows & columns in table
total_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
total_cols = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))
print("Total Rows in table : ",total_rows)
print("Total Columns in table: ",total_cols)

print()

# Read specific cell value
author_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[7]/td[2]").text
print("author name: ",author_name)

print()

# Read all table content as it is except first header row
for r in range(2,total_rows+1):
    for d in range(1,total_cols+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(d)+"]").text
        print(data,end = "---")
    print()

# Read data based on condition
for r in range(2,total_rows+1):
    author = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if author == "Amit":
        book_name = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        print(book_name,"--",author)
