import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("/home/abhivekariya/driver_for_browser/chrome/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

radio_buttons = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']/li")
total_radio_buttons = len(radio_buttons)

desired_option = "Dummy ticket for Visa Application"
for r in range(1, total_radio_buttons + 1):
    main_text = driver.find_element(By.XPATH, "//ul[@id='checkout-products']/li[" + str(r) + "]").text
    real_text = main_text.split("  —  ")[0]
    if real_text == desired_option:
        driver.find_element(By.XPATH, "//ul[@id='checkout-products']/li[" + str(r) + "]/label").click()

driver.find_element(By.CSS_SELECTOR, "input[id='travname']").send_keys("Kaushik")
driver.find_element(By.ID, "travlastname").send_keys("Patel")

# Find using nested element(tag.class tag#ID)
driver.find_element(By.CSS_SELECTOR, "span.woocommerce-input-wrapper textarea#order_comments").send_keys(
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")

driver.find_element(By.XPATH, "//input[@id='dob']").click()

dropdown_month = Select(driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-month"))
dropdown_month.select_by_visible_text("Dec")

dropdown_year = Select(driver.find_element(By.CSS_SELECTOR, "select.ui-datepicker-year"))
dropdown_year.select_by_visible_text("2002")

days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for day in days:
    if day.text == "9":
        day.click()

Gender = driver.find_elements(By.CSS_SELECTOR, "input[type='radio'][name='sex'] + label")

for g in Gender:
    if g.text == 'Female':
        g.click()

driver.find_element(By.XPATH, "//input[@id='addmorepax']").click()
driver.find_element(By.XPATH, "//input[@id='traveltype_2']").click()
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Mumbai")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Delhi")

driver.find_element(By.XPATH, "//input[@id='departon']").click()

departure_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
departure_month.select_by_visible_text("Aug")

departure_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
departure_year.select_by_visible_text("2024")

departure_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for d_date in departure_dates:
    if d_date.text == "22":
        d_date.click()

driver.find_element(By.XPATH, "//input[@id='returndate']").click()

return_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
return_month.select_by_visible_text("Nov")

return_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
return_year.select_by_visible_text("2024")

return_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for r_date in return_dates:
    if r_date.text == "13":
        r_date.click()

driver.find_element(By.XPATH, "//textarea[@name='notes']").send_keys(
    "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage,and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and"
    "1.10.33 of de Finibus Bonorum et Malorum(The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.."
    ", comes from a line in section 1.10.32.The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from de Finibus Bonorum et Malorum by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.")

driver.find_element(By.CSS_SELECTOR, "#select2-reasondummy-container").click()
driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys("Car")
driver.find_element(By.XPATH,"//li[contains(text(), 'Car rental')]").click()


# driver.find_element(By.XPATH,"//input[@id='appoinmentdate']").click()
# appointment_month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
# appointment_month.select_by_visible_text("Jul")
#
# appointment_year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
# appointment_year.select_by_visible_text("2025")
#
# appointment_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")
#
# for app_date in appointment_dates:
#     if app_date.text == '5':
#         app_date.click()

driver.find_element(By.XPATH, "//input[@id='deliverymethod_2']").click()

driver.find_element(By.XPATH,"//input[@id='billname']").send_keys("Bill_general_01")
driver.find_element(By.XPATH,"//input[@id='billing_phone']").send_keys("1478523990")
driver.find_element(By.XPATH,"//input[@id='billing_email']").send_keys("abcd@gmail.com")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys('Ir')
driver.find_element(By.XPATH, "//ul[@id='select2-billing_country-results']/li[3]").click()

driver.find_element(By.XPATH,"//input[@id='billing_address_1']").send_keys("ABC park, Main road, Kevalam valley")
driver.find_element(By.XPATH,"//input[@id='billing_address_2']").send_keys("Apartment 123, new road")

driver.find_element(By.XPATH,"//input[@id='billing_city']").send_keys("Surat")
driver.find_element(By.XPATH, "//input[@id='billing_state']").send_keys("Babil")

driver.find_element(By.XPATH,"//input[@id='billing_postcode']").send_keys("147000")

cart_subtotal = driver.find_element(By.XPATH,"//table[@class='shop_table woocommerce-checkout-review-order-table']/tfoot/tr/td/span")
cart_subtotal_rupees = cart_subtotal.text

order_total = driver.find_element(By.XPATH,"//tr[@class='order-total']//span[@class='woocommerce-Price-amount amount']")
order_total_rupees = order_total.text

if cart_subtotal_rupees == order_total_rupees:
    driver.find_element(By.XPATH,"//button[@id='place_order']").click()
else:
    print("Cart subtotal does not match order total")


# desired_option = "WhatsApp"
# for radio in range(1,total_buttons+1):
#      option = driver.find_element(By.XPATH,"//p[@id='deliverymethod_field']/span/input["+str(radio)+"]")
#      print(option.text)
#      if option.text == desired_option:
#          option.click()
#          break

#     # Identify the radio buttons
#     radio_buttons = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']")
#
#     # Iterate through the radio buttons and select the desired option
#     desired_option = "Dummy ticket for Visa Application"  # Specify the option you want to select
#     for radio in radio_buttons:
#         label_text = radio.find_element(By.XPATH, "//input[@id='product_549']").text
#         print(label_text.strip())
#         if label_text.strip() == desired_option:
#             radio.click()
#             break
#
#
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
#
# finally:
#     # Close the browser window
#     time.sleep(5)
#     driver.quit()
