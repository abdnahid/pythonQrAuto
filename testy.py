import time
import math
import pandas
import os
from en_words import EnWords
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pandas import Series
from actions import calc_fee
import inflect


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
word_engine=inflect.engine()

data = pandas.read_csv("daily.csv")
word_engine=inflect.engine()

insertedData = []

def insert_company(x:Series)->dict:
    return {
            "name":x["name"],
            "address":x.address,
            "thana":x.thana if x.thana !="none" else '',
            "district":x.district,
            "scales":[
                {"capacity":x.capacity,"type":x.type,"quantity":x.quantity,"model":x.model if x.model!="none" else "","brand":x.brand if x.brand!="none" else "","serial":x.serial if x.serial!="none" else ""},
            ],
            "receipt":x.receipt
        }

for i,x in data.iterrows():
    if len(insertedData)==0:
        insertedData.append(insert_company(x))
    else:
        matched_index=None
        for index,value in enumerate(insertedData):
            if value["name"]==x["name"] and value["address"]==x["address"]:
                matched_index=index
                insertedData[index]["scales"].append({"capacity":x.capacity,"type":x.type,"quantity":x.quantity,"model":x.model if x.model!="none" else "","brand":x.brand if x.brand!="none" else "","serial":x.serial if x.serial!="none" else ""})
        if matched_index ==None:
            insertedData.append(insert_company(x))

for i in insertedData:
    total_quantity=0
    subtotal = 0
    table_row_data=''
    for j,scale in enumerate(i["scales"]):
        total_quantity+=scale['quantity']
        fee = calc_fee(scale['capacity'])*scale['quantity']
        subtotal+=fee
        table_row_data+=f'<tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;">{(j+1)}</td><td style="width: 20%; border: 0.5px solid #000000;"><p>{scale['type']}</p><p>Brand: {"-" if scale['brand']=="none" else scale['brand']}</p></td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{f'{int(scale['capacity']*1000)}g' if scale['capacity']<1 else f'{int(scale['capacity'])}kg'}</td><td style="width: 10%; border: 0.5px solid #000000;">{scale['quantity']}</td><td style="width: 15%; border: 0.5px solid #000000;">-</td><td style="width: 10%; border: 0.5px solid #000000;">-</td><td style="width: 20%; border: 0.5px solid #000000;">{fee}</td></tr>'
    vat = math.ceil(subtotal*0.15)
    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;"><strong>Serial No</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>Description</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Capacity</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Quantity</strong></td><td style="width: 15%; border: 0.5px solid #000000;"><strong>Weight Denomination</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>Weight Class</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>Verification Fee (Taka)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">Subtotal</p></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{subtotal}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">15% VAT</p></td><td style="width: 18.0581%; text-align: center; border: 0.5px solid #000000;">{vat}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">Total</p></td><td style="width: 18.0581%; text-align: center; height: 54px; border: 0.5px solid #000000;">{vat+subtotal}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;"><strong><u>In Words: </u></strong> {word_engine.number_to_words(vat+subtotal)} taka only</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(2)
    driver.find_element(By.ID,"memo_no").send_keys("..605.31.003.21/"+i["name"])
    try:
        company_select_field = driver.find_element(By.XPATH,'//*[@id="company_id"]')
        Select(company_select_field).select_by_visible_text(i["name"])
        time.sleep(2)
        driver.find_element(By.ID,"verification_date").clear()
        driver.find_element(By.ID,"varification_address").clear()
        driver.find_element(By.ID,"equipment_verification").clear()
        driver.find_element(By.ID,"no_of_equipment").clear()
        driver.find_element(By.ID,"receipt_no").clear()
        driver.find_element(By.ID,"verification_date").clear()
    except:    
        driver.find_elements(By.NAME,"company_type")[0].click()
        time.sleep(1)
        driver.find_element(By.ID,"company_name").send_keys(i["name"])

    thana = i["thana"] if i["thana"]!="none" else "Select Thana"
    driver.find_element(By.ID,"varification_address").send_keys(i['address'])
    driver.find_element(By.ID,"verification_date").send_keys("26-03-2023")
    select_district = driver.find_element(By.ID,"verification_district_id")
    Select(select_district).select_by_visible_text(i['district'])
    time.sleep(2)
    select_thana = driver.find_element(By.ID,"verification_thana_id")
    try:
        Select(select_thana).select_by_visible_text(thana)
    except:
        Select(select_thana).select_by_visible_text("Select Thana")
    driver.find_element(By.ID,"equipment_verification").send_keys(total_quantity)
    driver.find_element(By.ID,"no_of_equipment").send_keys(total_quantity)
    time.sleep(1)
    driver.find_element(By.ID,"receipt_no").send_keys(i['receipt'])
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME,"tox-mbtn__select-label")[5].click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"tox-collection__item--active").click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME,"tox-textarea").clear()
    driver.find_element(By.CLASS_NAME,"tox-textarea").send_keys(table_data)
    driver.find_element(By.CSS_SELECTOR,"body > div.tox.tox-silver-sink.tox-tinymce-aux > div.tox-dialog-wrap > div.tox-dialog.tox-dialog--width-lg > div.tox-dialog__footer > div.tox-dialog__footer-end > button:nth-child(2)").click()
    driver.find_elements(By.NAME,"stamped_or_reject")[0].click()
    time.sleep(5)
    driver.find_element(
        By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-info.cancel"
    ).click()
    # driver.find_element(
    #     By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-primary"
    # ).click()

print("done")
