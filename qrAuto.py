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

driver.find_element(By.ID,'user_email').send_keys(os.getenv('LOGIN_EMAIL'))
driver.find_element(By.ID,'btnNext').click()

time.sleep(0.5)

driver.find_element(By.ID,'user_password').send_keys(os.getenv('ACCESS_KEY'))
time.sleep(0.5)
driver.find_element(By.ID,'btnSignIn').click()

time.sleep(0.5)





data = pandas.read_csv("data.csv")

for i,x in data.iterrows():
    capacity = x.capacity.split(',')
    quantity = x.quantity.split(',')
    quantity_int = [int(item) for item in quantity]
    total_quantity = sum(quantity_int)
    total_quantity_in_bn = Money(total_quantity).in_bn_letter()
    fees = x.fee.split(',')
    fees_in_bn_letter = [Money(i).in_bn_letter() for i in fees]
    fee_int = [int(item) for item in fees]
    subtotal = sum(fee_int)
    vat = math.ceil(sum(fee_int)*0.15)
    total = math.ceil(sum(fee_int)*1.15)
    money_instance = Money(str(total))
    total_in_words = money_instance.in_words()
    time.sleep(1)
    table_row_data=''
    for j,y in enumerate(capacity):
        table_row_data+=f'<tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;">{En2Bn(str(j+1)).translate()}</td><td style="width: 20%; border: 0.5px solid #000000;"><p>{x.type}</p><p>ব্রান্ডঃ {"-" if x.brand=="none" else x.brand}</p></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{y}</td><td style="width: 10%; border: 0.5px solid #000000;">{Money(quantity[j]).in_bn_letter()}</td><td style="width: 15%; border: 0.5px solid #000000;">{"-" if x.denomination=="none" else x.denomination}</td><td style="width: 10%; border: 0.5px solid #000000;">{"-" if x.weight_class=="none" else x.weight_class}</td><td style="width: 20%; border: 0.5px solid #000000;">{fees_in_bn_letter[j]}</td></tr>'
    time.sleep(1)
    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;"><strong>ক্রমিক নং</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>ওজন/পরিমাপণ ও পরিমাপণ যন্ত্রের বিবরণ</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>ওজন/ ধারণক্ষমতা</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>সংখ্যা/পরিমাণ</strong></td><td style="width: 15%; border: 0.5px solid #000000;"><strong>ওজন/পরিমাপণের ডিনোমিনেশন</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>ওজন/পরিমাপণের শ্রেণি</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>ভেরিফিকেশন ফি (টাকা)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">মোট</p></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{Money(subtotal).in_bn_letter()}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">১৫% ভ্যাট</p></td><td style="width: 18.0581%; text-align: center; border: 0.5px solid #000000;">{Money(vat).in_bn_letter()}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">সর্বমোট</p></td><td style="width: 18.0581%; text-align: center; height: 54px; border: 0.5px solid #000000;">{Money(total).in_bn_letter()}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;"><strong><u>কথায়ঃ</u></strong> {money_instance.words} টাকা মাত্র</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(2)
    driver.find_element(By.ID,"memo_no").send_keys(f'{x.memo}/{x["name"]}')
    try:
        company_select_field = driver.find_element(By.XPATH,'//*[@id="company_id"]')
        Select(company_select_field).select_by_visible_text(x["name"])
        time.sleep(2)
        driver.find_element(By.ID,"verification_date").clear()
        driver.find_element(By.ID,"varification_address").clear()
        driver.find_element(By.ID,"equipment_verification").clear()
        driver.find_element(By.ID,"equipment_verification").clear()
        driver.find_element(By.ID,"receipt_no").clear()
        driver.find_element(By.ID,"verification_date").clear()
    except:    
        driver.find_element(By.NAME,"company_type").click()
        time.sleep(1)
        driver.find_element(By.ID,"company_name").send_keys(x["name"])
    time.sleep(2)
    driver.find_element(By.ID,"varification_address").send_keys(x.address)
    time.sleep(1)
    driver.find_element(By.ID,"verification_date").send_keys("06-02-2023")
    select_district = driver.find_element(By.ID,"verification_district_id")
    Select(select_district).select_by_visible_text("Dhaka")
    time.sleep(1)
    select_thana = driver.find_element(By.ID,"verification_thana_id")
    Select(select_thana).select_by_visible_text("Kalabagan")
    driver.find_element(By.ID,"equipment_verification").send_keys(total_quantity_in_bn)
    driver.find_element(By.ID,"no_of_equipment").send_keys(total_quantity_in_bn)
    time.sleep(1)
    driver.find_element(By.ID,"receipt_no").send_keys(x.receipt)
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,"tox-mbtn__select-label")[5].click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"tox-collection__item--active").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"tox-textarea").clear()
    driver.find_element(By.CLASS_NAME,"tox-textarea").send_keys(table_data)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"body > div.tox.tox-silver-sink.tox-tinymce-aux > div.tox-dialog-wrap > div.tox-dialog.tox-dialog--width-lg > div.tox-dialog__footer > div.tox-dialog__footer-end > button:nth-child(2)").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#right_side_btn > button.btn.btn-info.cancel").click()

print('done')
