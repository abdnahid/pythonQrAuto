import time
import math
import pandas
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pandas import Series
from actions import calc_fee,get_scale_type
from bn_words import BnWords


load_dotenv()

MEMO_INIT="..605.31.003.21/"

# driver = webdriver.Firefox()
# driver.get(os.getenv("LOGIN_URL"))
# driver.maximize_window()


# time.sleep(0.5)

# driver.find_element(By.ID, "user_email").send_keys(os.getenv("LOGIN_EMAIL"))
# driver.find_element(By.ID, "btnNext").click()

# time.sleep(0.5)

# driver.find_element(By.ID, "user_password").send_keys(os.getenv("ACCESS_KEY"))
# time.sleep(0.5)
# driver.find_element(By.ID, "btnSignIn").click()

# time.sleep(0.5)

company_list=[]
allowed_scale_types = ["dw","ms","lm","wb"]

while True:
    name = input("Company Name: ")
    if name=="end":
        break
    address = input("Company Address: ")
    thana=input("Thana(leave empty if thana is not applicable): ")
    district=input("District: ")
    receipt=input("Verification fee receipt no: ")
    company = {
            "name":name,
            "address":address,
            "thana":thana,
            "district":district,
            "scales":[],
            "receipt":receipt
        }
    while True:
        scale_type = input("Scale Type ('dw' for digital weight scale, 'lm' for liter measures and 'ms' for meter scale): ")
        if scale_type=="end":
            break
        elif scale_type not in allowed_scale_types:
            continue
        else:
            print("Leave the following fields empty if not applicable")
            capacity=input("Capacity: ")
            quantity=input("Quantity: ")
            brand=input("Brand: ")
            model=input("Model: ")
            serial=input("Serial: ")
            company["scales"].append(
                    {"capacity":float(capacity),"type":get_scale_type(scale_type=scale_type),"quantity":int(quantity),"model":model,"brand":brand,"serial":serial},
                )
    company_list.append(company)
    

print(company_list)

for i in company_list:
    total_quantity=0
    subtotal = 0
    table_row_data=''
    for j,scale in enumerate(i["scales"]):
        total_quantity+=scale['quantity']
        fee = calc_fee(capacity=scale['capacity'],scale_type=scale['scale_type'])*scale['quantity']
        subtotal+=fee
        scaleType=f'<strong>Type:</strong> {scale['type']}'  if scale['type']!="" else ""
        brand=f', <strong>Brand:</strong> {scale['brand']}'  if scale['brand']!="" else ""
        model=f', <strong>Model:</strong> {scale['model']}'  if scale['model']!="" else ""
        serial=f', <strong>Serial:</strong> {scale['serial']}'  if scale['serial']!="" else ""
        
        table_row_data+=f'<tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;">{BnWords(str(j+1)).in_bn_letter()}</td><td style="width: 20%; border: 0.5px solid #000000;">{scaleType+brand+model+serial}</td><td style="width: 10%; text-align: center; border: 0.5px solid #000000;">{f'{BnWords(str(math.ceil(scale['capacity']*1000))).in_bn_letter()} গ্রাম' if scale['capacity']<1 else f'{BnWords(str(math.ceil(scale['capacity']))).in_bn_letter()} কেজি'}</td><td style="width: 10%; border: 0.5px solid #000000;">{BnWords(str(int(scale['quantity']))).in_bn_letter()}</td><td style="width: 15%; border: 0.5px solid #000000;">-</td><td style="width: 10%; border: 0.5px solid #000000;">-</td><td style="width: 20%; border: 0.5px solid #000000;">{BnWords(str(fee)).in_bn_letter()}</td></tr>'
    vat = math.ceil(subtotal*0.15)
    table_data = f'<p>&nbsp;</p><table style="border-collapse: collapse; width: 100%;" border="1"><tbody><tr style="text-align: center;"><td style="width: 8%; border: 0.5px solid #000000;"><strong>ক্রমিক</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>ওজন/পরিমাপযন্ত্রের বিবরণ</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>ধারণক্ষমতা</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>পরিমাণ</strong></td><td style="width: 15%; border: 0.5px solid #000000;"><strong>ওজন/পরিমাপযন্ত্রের ডিনোমিনেশন</strong></td><td style="width: 10%; border: 0.5px solid #000000;"><strong>ওজন/পরিমাপযন্ত্রের ক্লাস</strong></td><td style="width: 20%; border: 0.5px solid #000000;"><strong>ফি (টাকা)</strong></td></tr>{table_row_data}<tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">মোট</p></td><td style="width: 20%; text-align: center; border: 0.5px solid #000000;">{BnWords(str(subtotal)).in_bn_letter()}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">১৫% ভ্যাট</p></td><td style="width: 18.0581%; text-align: center; border: 0.5px solid #000000;">{BnWords(str(vat)).in_bn_letter()}</td></tr><tr><td style="text-align: center; width: 73%; border: 0.5px solid #000000;" colspan="6"><p style="text-align: right;">সর্বমোট</p></td><td style="width: 18.0581%; text-align: center; height: 54px; border: 0.5px solid #000000;">{BnWords(str(vat+subtotal)).in_bn_letter()}</td></tr><tr><td style="width: 93%;" colspan="7"><p style="text-align: left;"><strong><u>কথায়ঃ</u></strong> {BnWords(str(vat+subtotal)).in_words()} টাকা মাত্র</p></td></tr></tbody></table>'
    driver.get(os.getenv("VERIFICATION_URL"))
    time.sleep(2)
    driver.find_element(By.ID,"memo_no").send_keys("..605.31.003.21/"+i["name"])
        
    driver.find_elements(By.NAME,"company_type")[0].click()
    time.sleep(1)
    driver.find_element(By.ID,"company_name").send_keys(i["name"])

    thana = i["thana"] if i["thana"]!="none" else "Select Thana"
    driver.find_element(By.ID,"varification_address").send_keys(i['address'])
    driver.find_element(By.ID,"verification_date").send_keys("28-04-2024")
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
    # driver.find_element(
    #     By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-info.cancel"
    # ).click()
    # driver.find_element(
    #     By.CSS_SELECTOR, "#right_side_btn > button.btn.btn-primary"
    # ).click()

print("done")
