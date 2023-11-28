import time
import math
import pandas
import os
from taka import Money
from bn_number import En2Bn
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

load_dotenv()

driver = webdriver.Chrome()
driver.get(os.getenv("LOGIN_URL"))
driver.maximize_window()

time.sleep(0.5)

driver.find_element(By.ID, "user_email").send_keys(os.getenv("LOGIN_EMAIL"))
driver.find_element(By.ID, "btnNext").click()

time.sleep(0.5)

driver.find_element(By.ID, "user_password").send_keys(os.getenv("ACCESS_KEY"))
time.sleep(0.5)
driver.find_element(By.ID, "btnSignIn").click()

time.sleep(0.5)


data = pandas.read_csv("mithai.csv", encoding="windows-1252")

for i, x in data.iterrows():
    capacity = x.capacity
    quantity = x.quantity
    fees = int(x.fee)
    vat = math.ceil(fees * 0.15)
    total = math.ceil(fees * 1.15)
    money_instance = Money(str(total))
    total_in_words = money_instance.in_words()
    time.sleep(1)
    table_row_data = f'<tr style="text-align: center;"><td style="width: 8%; text-align: center; border: 0.5px solid #000000;">1</td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;"><p><strong>Type: </strong>{"Digital weight scale"}</p><p><strong>Brand:</strong> {"-" if x.brand=="none" else x.brand}</p></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{capacity} kg</td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{quantity}</td><td style="width: 15%; text-align: center; border: 0.5px solid #000000;">{"-" if x.denomination=="none" else x.denomination}</td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{"-" if x.weight_class=="none" else x.weight_class}</td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{x.fee}</td></tr>'

    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%; text-align: center; border: 0.5px solid #000000;"><strong>Serial No.</strong></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;"><strong>Details of Weight Scale</strong></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;"><strong>Capacity</strong></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;"><strong>Quantity</strong></td><td style="width: 15%; text-align: center; border: 0.5px solid #000000;"><strong>Weight Denomination</strong></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;"><strong>Weight Class</strong></td><td style="width: 20%; text-align:center; border: 0.5px solid #000000;"><strong>Verification Fee</strong></td></tr>{table_row_data}<tr><td style="text-align: right; width: 73%; border: 0.5px solid #000000;" colspan="6"><p>Subtotal</p></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{x.fee}</td></tr><tr><td style="text-align: right; width: 73%; border: 0.5px solid #000000;" colspan="6"><p>15% vat</p></td><td style="width: 18.0581%; text-align: center; border: 0.5px solid #000000;">{vat}</td></tr><tr><td style="text-align: right; width: 73%; border: 0.5px solid #000000;" colspan="6"><p>Total</p></td><td style="width: 18.0581%; text-align: center; height: 54px; border: 0.5px solid #000000;">{total}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left; padding:5px"><strong><u>কথায়ঃ</u></strong> {money_instance.words} টাকা মাত্র</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(2)
    driver.find_element(By.ID, "memo_no").send_keys(f'{x.memo}/{x["name"]}')
    try:
        company_select_field = driver.find_element(By.XPATH, '//*[@id="company_id"]')
        Select(company_select_field).select_by_visible_text(x["name"])
        time.sleep(2)
        driver.find_element(By.ID, "verification_date").clear()
        driver.find_element(By.ID, "varification_address").clear()
        driver.find_element(By.ID, "no_of_equipment").clear()
        driver.find_element(By.ID, "equipment_verification").clear()
        driver.find_element(By.ID, "receipt_no").clear()
        driver.find_element(By.ID, "verification_date").clear()
    except:
        driver.find_elements(By.NAME, "company_type")[0].click()
        time.sleep(1)
        driver.find_element(By.ID, "company_name").send_keys(x["name"])
    time.sleep(2)
    driver.find_element(By.ID, "varification_address").send_keys(x.address)
    time.sleep(1)
    driver.find_element(By.ID, "verification_date").send_keys("24-09-2023")
    select_district = driver.find_element(By.ID, "verification_district_id")
    Select(select_district).select_by_visible_text(x.district)
    time.sleep(2)
    select_thana = driver.find_element(By.ID, "verification_thana_id")
    Select(select_thana).select_by_visible_text("Select Thana")
    driver.find_element(By.ID, "equipment_verification").send_keys(quantity)
    driver.find_element(By.ID, "no_of_equipment").send_keys(quantity)
    time.sleep(1)
    driver.find_element(By.ID, "receipt_no").send_keys("354990")
    time.sleep(1)
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
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-info.cancel"
    ).click()
    time.sleep(2)

print("done")
