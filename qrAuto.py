import time
import math
import pandas
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import inflect

load_dotenv()

driver = webdriver.Chrome()
driver.get(os.getenv("LOGIN_URL"))
driver.maximize_window()
word_engine=inflect.engine()

time.sleep(0.5)

driver.find_element(By.ID, "user_email").send_keys(os.getenv("LOGIN_EMAIL"))
driver.find_element(By.ID, "btnNext").click()

time.sleep(0.5)

driver.find_element(By.ID, "user_password").send_keys(os.getenv("ACCESS_KEY"))
time.sleep(0.5)
driver.find_element(By.ID, "btnSignIn").click()

time.sleep(0.5)


data = pandas.read_csv("swapno.csv", encoding="windows-1252")

for i, x in data.iterrows():
    capacity = x.capacity.split(",")
    quantity = x.quantity.split(",")
    quantity_int = [int(item) for item in quantity]
    total_quantity = sum(quantity_int)
    fees = x.fee.split(",")
    fee_int = [int(item) for item in fees]
    subtotal = sum(fee_int)
    vat = math.ceil(sum(fee_int) * 0.15)
    total = math.ceil(sum(fee_int) * 1.15)
    time.sleep(1)
    table_row_data = ""
    for j, y in enumerate(capacity):
        table_row_data += f'<tr style="text-align: center;"><td style="width: 8%;text-align: center; border: 0.5px solid #000000;">{j+1}</td><td style="width: 20%;text-align: center; border: 0.5px solid #000000;"><p>Digital Weight Scale</p></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{y}</td><td style="width: 10%; border: 0.5px solid #000000;">{quantity[j]}</td><td style="width: 15%;text-align: center; border: 0.5px solid #000000;">-</td><td style="width: 10%;text-align: center; border: 0.5px solid #000000;">-</td><td style="width: 20%;text-align: center; border: 0.5px solid #000000;">{fees[j]}</td></tr>'
    time.sleep(1)
    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;"><strong>Serial</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>Details Of Weight Scale</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Capacity</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Quantity</strong></td><td style="width: 15%; border: 0.5px solid #000000;"><strong>Weight Denomination</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Weight Class</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>Verification Fee (taka)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">total (taka)</p></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{subtotal}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">15% vat (taka)</p></td><td style="width: 18.0581%; text-align: center; border: 0.5px solid #000000;">{vat}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">Grand Total</p></td><td style="width: 18.0581%; text-align: center; height: 54px; border: 0.5px solid #000000;">{total}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;"><strong><u>In Words</u></strong> {word_engine.number_to_words(total)} taka only</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(1)
    driver.find_element(By.ID, "memo_no").send_keys(f'..605.31.003.21/{x["name"]}')
    driver.find_elements(By.NAME, "company_type")[0].click()
    time.sleep(1)
    driver.find_element(By.ID, "company_name").send_keys(x["name"])
    time.sleep(1)
    driver.find_element(By.ID, "varification_address").send_keys(x.address)
    time.sleep(1)
    driver.find_element(By.ID, "verification_date").send_keys("14-11-23")
    select_district = driver.find_element(By.ID, "verification_district_id")
    Select(select_district).select_by_visible_text(x.district)
    time.sleep(1)
    select_thana = driver.find_element(By.ID, "verification_thana_id")
    Select(select_thana).select_by_visible_text("Select Thana")
    driver.find_element(By.ID, "equipment_verification").send_keys(total_quantity)
    driver.find_element(By.ID, "no_of_equipment").send_keys(total_quantity)
    time.sleep(1)
    driver.find_element(By.ID, "receipt_no").send_keys("356861")
    time.sleep(5)
    driver.find_elements(By.CLASS_NAME, "tox-mbtn__select-label")[5].click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "tox-collection__item--active").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "tox-textarea").clear()
    driver.find_element(By.CLASS_NAME, "tox-textarea").send_keys(table_data)
    driver.find_element(
        By.CSS_SELECTOR,
        "body > div.tox.tox-silver-sink.tox-tinymce-aux > div.tox-dialog-wrap > div.tox-dialog.tox-dialog--width-lg > div.tox-dialog__footer > div.tox-dialog__footer-end > button:nth-child(2)",
    ).click()
    driver.find_elements(By.NAME, "stamped_or_reject")[0].click()
    time.sleep(1)
    driver.find_element(
        By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-info.cancel"
    ).click()
    # driver.find_element(
    #     By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-primary"
    # ).click()

print("done")
