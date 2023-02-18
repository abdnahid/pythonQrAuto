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
    fees = x.fee.split(',')
    fee_int = [int(item) for item in fees]
    subtotal = sum(fee_int)
    total = math.ceil(sum(fee_int)*1.15)
    money_instance = Money(total)
    total_in_words = money_instance.in_words()
    time.sleep(1)
    table_row_data=''
    for j,y in enumerate(capacity):
        table_row_data+=f'<tr style="text-align: center;"><td style="width: 8%;">{j+1}</td><td style="width: 20%;"><p>{x.type}</p><p>ব্রান্ডঃ {"-" if x.brand=="none" else x.brand}</p></td><td style="width: 10%; text-align: center;">{y}</td><td style="width: 10%;">{quantity[j]}</td><td style="width: 15%;">{"-" if x.denomination=="none" else x.denomination}</td><td style="width: 10%;">{"-" if x.weight_class=="none" else x.weight_class}</td><td style="width: 20%;">{fee_int[j]}</td></tr>'
    time.sleep(1)
    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%;"><strong>ক্রমিক নং</strong></td><td style="width: 20%;"><strong>ওজন/পরিমাপণ ও পরিমাপণ যন্ত্রের বিবরণ</strong></td><td style="width: 10%;"><strong>ওজন/ ধারণক্ষমতা</strong></td><td style="width: 10%;"><strong>সংখ্যা/পরিমাণ</strong></td><td style="width: 15%;"><strong>ওজন/পরিমাপণের ডিনোমিনেশন</strong></td><td style="width: 10%;"><strong>ওজন/পরিমাপণের শ্রেণি</strong></td><td style="width: 20%;"><strong>ভেরিফিকেশন ফি (টাকা)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%;" colspan="6"><p style="text-align: right;">মোট</p></td><td style="width: 20%; text-align: center;">{subtotal}</td></tr><tr><td style="text-align: center; width: 73%;" colspan="6"><p style="text-align: right;">১৫% ভ্যাট</p></td><td style="width: 18.0581%; text-align: center;">{math.ceil(sum(fee_int)*0.15)}</td></tr><tr><td style="text-align: center; width: 73%;" colspan="6"><p style="text-align: right;">সর্বমোট</p></td><td style="width: 18.0581%; text-align: center; height: 54px;">{total}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;">{money_instance.words}</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(2)
    driver.find_element(By.ID,"memo_no").send_keys(x.memo)
    try:
        select_field = driver.find_element(By.XPATH,'//*[@id="company_id"]')
        Select(select_field).select_by_visible_text(x["name"])
    except:    
        driver.find_element(By.NAME,"company_type").click()
        time.sleep(1)
        driver.find_element(By.ID,"company_name").send_keys(x["name"])
    time.sleep(2)
    driver.find_element(By.ID,"varification_address").send_keys(x.address)
    time.sleep(1)
    driver.find_element(By.ID,"equipment_verification").send_keys(x.quantity)
    time.sleep(1)
    driver.find_element(By.ID,"receipt_no").send_keys(x.receipt)
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,"tox-mbtn__select-label")[5].click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"tox-collection__item--active").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"tox-textarea").send_keys(table_data)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"body > div.tox.tox-silver-sink.tox-tinymce-aux > div.tox-dialog-wrap > div.tox-dialog.tox-dialog--width-lg > div.tox-dialog__footer > div.tox-dialog__footer-end > button:nth-child(2)").click()
    time.sleep(2)

print('done')
